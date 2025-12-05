import speech_recognition as sr
import time
import os
import numpy as np
import io
import soundfile as sf
from pydub import AudioSegment
import librosa
from sklearn.cluster import KMeans


# ================================================================
#               ADVANCED FEATURE EXTRACTION
# ================================================================

def extract_features(wav_bytes):
    """Extract MFCC + Chroma + Contrast + Tonnetz + Pitch + Energy."""
    try:
        audio_buffer = io.BytesIO(wav_bytes)
        y, sr = sf.read(audio_buffer)

        if len(y.shape) > 1:
            y = np.mean(y, axis=1)

        y = y / (np.max(np.abs(y)) + 1e-9)

        # MFCC (13)
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)

        # Chroma (12)
        stft = np.abs(librosa.stft(y))
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr), axis=1)

        # Spectral Contrast (7)
        contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sr), axis=1)

        # Tonnetz (6)
        tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr), axis=1)

        # Pitch
        pitches, _ = librosa.piptrack(y=y, sr=sr)
        pitch_val = np.mean(pitches[pitches > 0]) if np.any(pitches > 0) else 0

        # Energy
        energy = np.sum(y ** 2)

        # Combine embedding
        embedding = np.hstack([mfcc, chroma, contrast, tonnetz, pitch_val, energy])
        return embedding

    except Exception as e:
        print("Feature error:", e)
        return None


# ================================================================
#                   SPEAKER CLUSTERING + MATCHING
# ================================================================

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def match_speaker(embedding, speaker_db, kmeans_model, threshold=0.80):
    """
    Improved: uses KMeans + similarity threshold.
    """
    if not speaker_db:
        return "Speaker 1"

    # Cluster prediction
    cluster = kmeans_model.predict([embedding])[0]

    # List all speakers in this cluster
    possible_speakers = [
        spk for spk, data in speaker_db.items() if data["cluster"] == cluster
    ]

    if not possible_speakers:
        return f"Speaker {len(speaker_db) + 1}"

    # Compare cosine similarity with speakers inside same cluster
    best_score = -1
    best_spk = None

    for spk in possible_speakers:
        avg_embed = np.mean(speaker_db[spk]["embeddings"], axis=0)
        score = cosine_similarity(avg_embed, embedding)

        if score > best_score:
            best_score = score
            best_spk = spk

    # Dynamic thresholding
    dynamic_threshold = max(0.75, threshold * (1 + 0.1 * np.random.rand()))

    if best_score >= dynamic_threshold:
        return best_spk

    return f"Speaker {len(speaker_db) + 1}"


# ================================================================
#                      DUPLICATE DETECTION
# ================================================================

def is_duplicate(new_chunk: str, last_chunk: str) -> bool:
    if not last_chunk:
        return False
    n = new_chunk.lower().strip()
    l = last_chunk.lower().strip()
    if n == l or n in l or l in n:
        return True
    return False


# ================================================================
#                          MAIN SYSTEM
# ================================================================

def start_live_stt():
    recognizer = sr.Recognizer()
    print("LIVE STT + IMPROVED SPEAKER RECOGNITION (KMeans + Multi-Features)")
    print("------------------------------------------------------------------")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Noise calibration completed.\n")

        speaker_db = {}  # {speaker_id: {"embeddings": [], "cluster": int}}
        embeddings_all = []
        kmeans_model = None
        num_clusters = 5  # max speakers expected

        while True:
            cmd = input("Press Enter to start, 'q' to quit: ").strip().lower()
            if cmd == "q":
                break

            print("\n🎙 Recording... Speak.")
            print("Press Ctrl + C to stop.\n")

            full_text = ""
            last_chunk = ""
            full_audio = AudioSegment.empty()
            speaker_history = []  # for smoothing (majority vote)

            try:
                while True:
                    audio = recognizer.listen(source, phrase_time_limit=4)
                    wav_bytes = audio.get_wav_data()

                    # Add to final audio
                    full_audio += AudioSegment(
                        data=wav_bytes,
                        sample_width=2,
                        frame_rate=16000,
                        channels=1
                    )

                    # Extract embedding
                    embedding = extract_features(wav_bytes)
                    if embedding is None:
                        continue

                    embeddings_all.append(embedding)

                    # Train/update KMeans clustering
                    if len(embeddings_all) >= num_clusters:
                        kmeans_model = KMeans(
                            n_clusters=min(num_clusters, len(embeddings_all)),
                            n_init=10
                        )
                        kmeans_model.fit(embeddings_all)

                    # Determine speaker
                    if kmeans_model:
                        speaker = match_speaker(embedding, speaker_db, kmeans_model)
                    else:
                        speaker = "Speaker 1"

                    # Update database
                    speaker_db.setdefault(speaker, {"embeddings": [], "cluster": 0})
                    speaker_db[speaker]["embeddings"].append(embedding)

                    if kmeans_model:
                        speaker_db[speaker]["cluster"] = int(
                            kmeans_model.predict([embedding])[0]
                        )

                    print(f"🔊 Identified: {speaker}")

                    # Speech recognition
                    try:
                        text = recognizer.recognize_google(audio)
                        print("Chunk:", text)

                        if is_duplicate(text, last_chunk):
                            print("→ Duplicate skipped.\n")
                            continue

                        full_text += f"\n[{speaker}] {text}"
                        last_chunk = text

                        print(full_text)
                        print()

                    except sr.UnknownValueError:
                        print("?? Unrecognized speech\n")
                    except sr.RequestError as e:
                        print("API error:", e)
                        break

            except KeyboardInterrupt:
                print("\n🛑 Stopped recording.")

            # Save outputs
            os.makedirs("output_improved", exist_ok=True)
            timestamp = int(time.time())

            audio_path = f"output_improved/final_audio_{timestamp}.wav"
            text_path = f"output_improved/final_text_{timestamp}.txt"

            full_audio.export(audio_path, format="wav")
            print(f"🎵 Saved: {audio_path}")

            if full_text.strip():
                with open(text_path, "w", encoding="utf-8") as f:
                    f.write(full_text.strip())
                print(f"💾 Saved: {text_path}")

            print("\n---------------------------------------------\n")


# ================================================================
#                          RUN SYSTEM
# ================================================================

if __name__ == "__main__":
    start_live_stt()
