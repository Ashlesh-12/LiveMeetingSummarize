import speech_recognition as sr
import time
import os
from pydub import AudioSegment

# ======================================================================
# ------------------------ DUPLICATE DETECTION --------------------------
# ======================================================================

def is_duplicate(new_chunk: str, last_chunk: str) -> bool:
    if not last_chunk:
        return False

    n = new_chunk.lower().strip()
    l = last_chunk.lower().strip()

    if n == l:
        return True
    if n in l or l in n:
        return True

    n_words = n.split()
    l_words = l.split()

    if len(n_words) < 3 or len(l_words) < 3:
        return False

    n_first3 = " ".join(n_words[:3])
    n_last3  = " ".join(n_words[-3:])
    l_first3 = " ".join(l_words[:3])
    l_last3  = " ".join(l_words[-3:])

    if n_first3 == l_last3 or n_last3 == l_first3:
        return True

    return False


# ======================================================================
# ---------------------------- MAIN LOGIC -------------------------------
# ======================================================================

def start_live_stt():
    recognizer = sr.Recognizer()

    print("Live Speech-to-Text (Final Audio + Text Saving Only)")
    print("-----------------------------------------------------------")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ambient noise adjusted.\n")

        while True:
            cmd = input("Press Enter to START recording, or 'q' to quit: ").strip().lower()
            if cmd == "q":
                print("Exiting...")
                break

            print("\n🎙 Recording started. Speak now.")
            print("To STOP, press Ctrl + C.\n")

            full_text = ""
            last_chunk = ""

            # Record full audio using Pydub
            print("Recording full audio...")
            full_audio = AudioSegment.empty()

            try:
                while True:
                    try:
                        print("Listening...")
                        audio = recognizer.listen(source, phrase_time_limit=6)

                        # Append raw audio
                        full_audio += AudioSegment(
                            data=audio.get_wav_data(),
                            sample_width=2,
                            frame_rate=16000,
                            channels=1
                        )

                        print("Recognizing...")
                        text = recognizer.recognize_google(audio)
                        print("Chunk:", text)

                        # Duplicate check
                        if is_duplicate(text, last_chunk):
                            print("→ Skipped duplicate.\n")
                            continue

                        # Merge text
                        full_text = (full_text + " " + text).strip()
                        last_chunk = text

                        print("→ Current merged text:")
                        print(full_text)
                        print()

                    except sr.UnknownValueError:
                        print("Could not understand audio...\n")
                    except sr.RequestError as e:
                        print("API Error:", e)
                        break

            except KeyboardInterrupt:
                print("\n🛑 Recording stopped.")

            # ============================
            # Save Final Audio + Text
            # ============================
            os.makedirs("output", exist_ok=True)
            timestamp = int(time.time())

            # Save audio
            audio_path = f"output/final_audio_{timestamp}.wav"
            full_audio.export(audio_path, format="wav")
            print(f"\n🎵 Final audio saved to: {audio_path}")

            # Save text
            if full_text:
                text_path = f"output/final_text_{timestamp}.txt"
                with open(text_path, "w", encoding="utf-8") as f:
                    f.write(full_text)
                print(f"💾 Final text saved to: {text_path}")
            else:
                print("(No valid text to save.)")

            print("\n-------------------------------------------\n")


# ======================================================================
# --------------------------- START PROGRAM -----------------------------
# ======================================================================

if __name__ == "__main__":
    start_live_stt()
