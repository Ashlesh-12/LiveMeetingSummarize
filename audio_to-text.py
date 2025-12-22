import sounddevice as sd
import queue
import json
import time
import wave
from vosk import Model, KaldiRecognizer

model_path = 'D:/Infosys_Springboard/AI_Internship/vosk-model'
vosk_model = Model(model_path)
rec = KaldiRecognizer(vosk_model, 16000)

q = queue.Queue()

duration = 10  # seconds

# File where audio will be saved
output_file = "recorded_audio.wav"

wf = wave.open(output_file, 'wb')
wf.setnchannels(1)
wf.setsampwidth(2)
wf.setframerate(16000)

def callback(indata, frames, time_info, status):
    q.put(bytes(indata))

with sd.RawInputStream(
    samplerate=16000,
    blocksize=4000,
    dtype='int16',
    channels=1,
    callback=callback
):

    print("Listening... speak now")

    start = time.time()
    result=""

    while time.time() - start < duration:
        data = q.get()

        wf.writeframes(data)

        if rec.AcceptWaveform(data):
            text = json.loads(rec.Result()).get("text")
            if text:
                result += text + " "

# Final cleanup recognition
final_text = json.loads(rec.FinalResult()).get("text")
if final_text:
    result += final_text

wf.close()

print("Final Output:", result)