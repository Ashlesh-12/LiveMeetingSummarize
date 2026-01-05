# run this first !pip install gTTS
from gtts import gTTS
text=open("text.txt").read()
tts=gTTS(text=text,lang='en')
tts.save("speech.mp3")
