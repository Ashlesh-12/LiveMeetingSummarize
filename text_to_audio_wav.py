# first run this !pip install gTTS soundfile

from gtts import gTTS
from IPython.display import Audio,display
import soundfile as sf
import numpy as np
text="hello this is an automatically genrated audio message created in google colab"
tts=gTTS(text=text,lang="en")
tts.save("text_audio.mp3")
import librosa
audio_data,sr=librosa.load("text_audio.mp3",sr=16000)
sf.write("text_audio.wav",audio_data,sr)
print("text converted to speeh and saved as 'text_audio.wav'")
display(Audio("text_audio.wav",autoplay=False))
