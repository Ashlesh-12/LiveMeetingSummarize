# run this first "pip install numpy soundfile"

import numpy as np
import soundfile as sf
from IPython.display import Audio,display
duration=3
sample_rate=16000
frequency=440
t=np.linspace(0,duration,int(sample_rate*duration),endpoint=False)
audio_data=0.5*np.sin(2*np.pi*frequency*t)
output_file="genrated_audio.wav"
sf.write(output_file,audio_data,sample_rate)
print("audio file created successfully")
print("saved as",output_file)
display(Audio(output_file,autoplay=True))
