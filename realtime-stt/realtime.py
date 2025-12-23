import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import jiwer
from datetime import datetime

# Create logs folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Audio settings
samplerate = 16000
device = None  # default input device
model = vosk.Model("D:/Infosys_Springboard/AI_Internship/vosk-model")  # make sure you downloaded a Vosk model into ./model

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# Start stream
with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device,
                       dtype="int16", channels=1, callback=callback):

    rec = vosk.KaldiRecognizer(model, samplerate)
    print("[Info] Real-time STT loop started. Speak into your microphone.")

    full_transcript = ""

    try:
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if result.get("text"):
                    print("[Final]", result["text"])
                    full_transcript += result["text"] + "\n"
            else:
                partial = json.loads(rec.PartialResult())
                if partial.get("partial"):
                    print("[Partial]", partial["partial"])
    except KeyboardInterrupt:
        print("[Info] Stop requested.")

    # Save transcript
    hyp_path = "logs/transcript.txt"
    with open(hyp_path, "w", encoding="utf-8") as f:
        f.write(full_transcript.strip())
    print("[Info] Transcript saved to:", hyp_path)

    # -----------------------------
    # WER Evaluation Block (ADDED)
    # -----------------------------
    ref_path = "logs/reference.txt"
    metrics_path = "logs/run_metrics.txt"

    if os.path.exists(ref_path) and os.path.exists(hyp_path):
        with open(ref_path, "r", encoding="utf-8") as f:
            reference = f.read().strip()
        with open(hyp_path, "r", encoding="utf-8") as f:
            hypothesis = f.read().strip()

        # Compute WER
        wer = jiwer.wer(reference, hypothesis)

        # Write results
        with open(metrics_path, "a", encoding="utf-8") as f:
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write(f"Reference length: {len(reference.split())} words\n")
            f.write(f"Hypothesis length: {len(hypothesis.split())} words\n")
            f.write(f"WER: {wer:.2f}\n\n")

        print(f"[Eval] WER computed: {wer:.2f}")
    else:
        print("[Eval] No reference.txt found. Skipping WER.")