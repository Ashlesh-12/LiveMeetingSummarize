# app.py
import streamlit as st
import tempfile, os, json, contextlib, wave, subprocess
from pathlib import Path
from datetime import timedelta
import whisper
import webrtcvad
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

st.set_page_config(page_title="Multilang Meeting Assistant", layout="wide")
st.title("🎙️ Multilingual Meeting Assistant (ffmpeg-based)")

st.markdown("""
Upload audio (wav/mp3/m4a). The app converts it to 16k mono WAV using ffmpeg (no pydub required),
runs VAD to find speech segments, transcribes each with Whisper, and attempts language detection.
""")

################ Sidebar controls
st.sidebar.header("Settings")
model_name = st.sidebar.selectbox("Whisper model", ["tiny", "base", "small", "medium"], index=2)
vad_aggressiveness = st.sidebar.slider("VAD aggressiveness (0-3)", 0, 3, 2)
min_segment_s = st.sidebar.slider("Min segment length for language-detect (s)", 1, 3, 1)
st.sidebar.caption("Requires ffmpeg on PATH")

################ Helpers
def run_ffmpeg_convert_to_wav(input_path, out_wav_path):
    # convert to 16k, mono, pcm_s16le wav
    cmd = [
        "ffmpeg", "-y", "-i", str(input_path),
        "-ar", "16000", "-ac", "1", "-vn",
        "-acodec", "pcm_s16le",
        str(out_wav_path)
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg convert failed: {proc.stderr.decode('utf-8')}")

def run_ffmpeg_extract_chunk(in_wav, start_s, end_s, out_path):
    # use -ss and -to for accurate extraction; requires ffmpeg
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start_s),
        "-to", str(end_s),
        "-i", str(in_wav),
        "-ar", "16000", "-ac", "1",
        "-acodec", "pcm_s16le",
        str(out_path)
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg chunk failed: {proc.stderr.decode('utf-8')}")

def vad_segments_from_wav(wav_path, aggressiveness=2, frame_duration_ms=30):
    vad = webrtcvad.Vad(aggressiveness)
    segments = []
    with contextlib.closing(wave.open(wav_path, 'rb')) as wf:
        assert wf.getnchannels() == 1, "Audio must be mono WAV"
        sample_rate = wf.getframerate()
        frame_size = int(sample_rate * frame_duration_ms / 1000.0)
        i = 0
        triggered = False
        voiced_frames = []
        start_time = 0.0
        while True:
            frames = wf.readframes(frame_size)
            if not frames:
                break
            is_speech = vad.is_speech(frames, sample_rate)
            timestamp = (i * frame_duration_ms) / 1000.0
            if is_speech and not triggered:
                triggered = True
                start_time = timestamp
                voiced_frames = [frames]
            elif is_speech and triggered:
                voiced_frames.append(frames)
            elif not is_speech and triggered:
                end_time = timestamp + (frame_duration_ms / 1000.0)
                segments.append((start_time, end_time))
                triggered = False
                voiced_frames = []
            i += 1
        if triggered and voiced_frames:
            end_time = (i * frame_duration_ms) / 1000.0
            segments.append((start_time, end_time))
    # merge small gaps
    merged = []
    if segments:
        cur_s, cur_e = segments[0]
        for s,e in segments[1:]:
            if s - cur_e <= 0.5:
                cur_e = e
            else:
                merged.append((cur_s, cur_e))
                cur_s, cur_e = s, e
        merged.append((cur_s, cur_e))
    return merged

def format_timespan(seconds):
    delta = timedelta(seconds=seconds)
    total_seconds = delta.total_seconds()
    hrs = int(total_seconds // 3600)
    mins = int((total_seconds % 3600) // 60)
    secs = total_seconds % 60
    return f"{hrs:02d}:{mins:02d}:{secs:06.3f}"

def to_srt(transcript_segments):
    lines = []
    for i, seg in enumerate(transcript_segments, start=1):
        s = format_timespan(seg["start"]).replace('.',',')
        e = format_timespan(seg["end"]).replace('.',',')
        lang = seg.get("language","unknown")
        text = seg.get("text","")
        lines.append(str(i))
        lines.append(f"{s} --> {e}")
        lines.append(f"[{lang}] {text}")
        lines.append("")
    return "\n".join(lines)

def transcribe_with_whisper(model, wav_path, segments, min_segment_s=1):
    results = []
    # Whisper model already loaded
    for idx, (start, end) in enumerate(segments):
        # make sure segment not too short for language detection
        if (end - start) < min_segment_s:
            end = min(end + (min_segment_s - (end - start)), get_wav_duration(wav_path))
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
            seg_path = tf.name
        run_ffmpeg_extract_chunk(wav_path, start, end, seg_path)
        try:
            trans = model.transcribe(seg_path, language=None, task="transcribe")
            text = trans.get("text", "").strip()
            detected_lang = trans.get("language", None)
        except Exception as e:
            text = ""
            detected_lang = None
        if not detected_lang and text:
            try:
                detected_lang = detect(text)
            except Exception:
                detected_lang = None
        results.append({
            "index": idx,
            "start": start,
            "end": end,
            "text": text,
            "language": detected_lang
        })
        try:
            os.remove(seg_path)
        except OSError:
            pass
    return results

def get_wav_duration(wav_path):
    with contextlib.closing(wave.open(wav_path,'rb')) as wf:
        return wf.getnframes() / wf.getframerate()

################ UI
uploaded = st.file_uploader("Upload audio file (wav/mp3/m4a/ogg/flac)", type=["wav","mp3","m4a","ogg","flac"])
run_btn = st.button("Transcribe")

if uploaded:
    st.audio(uploaded, format=uploaded.type)

if run_btn and uploaded:
    tmp_dir = tempfile.mkdtemp()
    try:
        local_in = Path(tmp_dir) / uploaded.name
        # save uploaded to disk
        with open(local_in, "wb") as f:
            f.write(uploaded.getbuffer())

        wav_path = Path(tmp_dir) / "converted_16k_mono.wav"
        st.info("Converting audio to 16k mono WAV using ffmpeg...")
        try:
            run_ffmpeg_convert_to_wav(local_in, wav_path)
        except Exception as e:
            st.error(f"ffmpeg conversion failed: {e}")
            raise

        duration = get_wav_duration(str(wav_path))
        st.success(f"Converted. Duration: {duration:.1f} s")

        st.info("Running VAD to find speech segments...")
        segments = vad_segments_from_wav(str(wav_path), aggressiveness=vad_aggressiveness)
        st.write(f"Detected {len(segments)} speech segments (merged).")
        st.dataframe([{"idx":i, "start":s, "end":e, "len_s":e-s} for i,(s,e) in enumerate(segments)])

        with st.spinner(f"Loading Whisper model '{model_name}'..."):
            model = whisper.load_model(model_name)

        with st.spinner("Transcribing segments... (this can take a while)"):
            transcript_segments = transcribe_with_whisper(model, str(wav_path), segments, min_segment_s=min_segment_s)

        st.success("Transcription done.")
        # show
        for seg in transcript_segments:
            start = format_timespan(seg["start"])
            end = format_timespan(seg["end"])
            lang = seg.get("language") or "unknown"
            with st.expander(f"[{start} → {end}] ({lang}) — {seg['text'][:60]}...", expanded=False):
                st.write(seg["text"])
                st.write(f"Language: **{lang}**")

        base = Path(uploaded.name).stem
        out_json = json.dumps(transcript_segments, indent=2, ensure_ascii=False)
        out_srt = to_srt(transcript_segments)
        out_txt = "\n\n".join([f"[{format_timespan(s['start'])} - {format_timespan(s['end'])}] ({s.get('language','')})\n{s['text']}" for s in transcript_segments])

        st.download_button("Download JSON", data=out_json, file_name=f"{base}_transcript.json", mime="application/json")
        st.download_button("Download SRT", data=out_srt, file_name=f"{base}.srt", mime="text/plain")
        st.download_button("Download TXT", data=out_txt, file_name=f"{base}_transcript.txt", mime="text/plain")
    finally:
        # optional: keep tmp for debugging; remove if desired
        pass
