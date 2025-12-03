import queue, sys, json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# Change this to the path where you extracted the VOSK model
MODEL_PATH = r"C:\Users\divya\OneDrive\Desktop\live\vosk-model-small-en-us-0.15"

# audio settings
SAMPLE_RATE = 16000
CHANNELS = 1
BLOCKSIZE = 4000  

def main():
    print("Loading model from:", MODEL_PATH)
    model = Model(MODEL_PATH)
    rec = KaldiRecognizer(model, SAMPLE_RATE)
    rec.SetWords(False)  

    q = queue.Queue()

    def audio_callback(indata, frames, time, status):
        """This callback runs in a separate thread from sounddevice."""
        if status:
            # print status (optional)
            print(status, file=sys.stderr)
        # indata is numpy array; convert to bytes
        q.put(bytes(indata))

    print("Input device:", sd.query_devices(kind='input')['name'])
    print("Listening (press Ctrl+C to stop)...\n")

    transcript = ""       
    prev_partial = ""     

    try:
        with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=BLOCKSIZE,
                               dtype='int16', channels=CHANNELS,
                               callback=audio_callback):
            while True:
                data = q.get()  # blocking
                if rec.AcceptWaveform(data):
                    # final result arrived
                    r = json.loads(rec.Result())
                    text = r.get("text", "").strip()
                    if text:
                        # append final text to our transcript
                        if transcript:
                            transcript = transcript + " " + text
                        else:
                            transcript = text
                        prev_partial = ""
                        # print final transcript (you can save to file instead)
                        print("\n[FINAL]  " + transcript)
                else:
                    # partial result arrived
                    p = json.loads(rec.PartialResult()).get("partial", "").strip()
                    # only update output when partial changes (to reduce flicker)
                    if p != prev_partial:
                        prev_partial = p
                        # merged view = confirmed transcript + current partial
                        if transcript and p:
                            merged = (transcript + " " + p).strip()
                        elif p:
                            merged = p
                        else:
                            merged = transcript
                        # use carriage return to overwrite the same line (nice CLI UX)
                        sys.stdout.write("\r[PARTIAL] " + merged + " " * 10)
                        sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print("\nError:", str(e))

if __name__ == "__main__":
    main()