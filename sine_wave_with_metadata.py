# run this first !pip install soundfile mutagen

import numpy as np
from IPython.display import Audio,display
import soundfile as sf
from mutagen.wave import WAVE
from mutagen.id3 import TextFrame
duration=3
sample_rate=16000
frequency=440
t=np.linspace(0,duration,int(sample_rate*duration),endpoint=False)
audio_data=0.5*np.sin(2*np.pi*frequency*t)
output_file="genrated_audio.wav"
sf.write(output_file,audio_data,sample_rate)
metadata=WAVE(output_file)
metadata["INAM"]=TextFrame(encoding=3,text=["Sample tone audio"])
metadata["IART"]=TextFrame(encoding=3,text=["Your Name"])
metadata["ICMT"]=TextFrame(encoding=3,text=["this is genratednaudio tone with embedded metadata"])
metadata["ICRD"]=TextFrame(encoding=3,text=["2025-02-14"])
metadata.save()
print("audio file created with metadata")
display(Audio(output_file,autoplay=False))
print("===embedded metadata in wav file===")
for key,value in metadata.items():
  print(f"{key}:{value.text[0] if hasattr(value,'text')else vale}")
