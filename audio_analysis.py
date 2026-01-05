import librosa
import numpy as np
import matplotlib.pyplot as plt
audio,sr=librosa.load('/content/groovy-vibe-427121.mp3')
amplitude=np.abs(audio)
n_fft=2048
hop_length=512
stft=np.abs(librosa.stft(audio,n_fft=n_fft,hop_length=hop_length))
freqs=np.mean(stft,axis=1)
times=librosa.frames_to_time(np.arange(stft.shape[1]),sr=sr,hop_length=hop_length)
plt.figure(figsize=(12,6))
plt.plot(np.arange(len(audio))/sr,amplitude)
plt.xlabel("time(s)")
plt.ylabel("amlitude")
plt.title("amplitude over time")
plt.show()
plt.figure(figsize=(12,6))
plt.imshow(librosa.amplitude_to_db(stft,ref=np.max),cmap='magma',origin='lower',aspect='auto')
plt.xlabel("time(s)")
plt.ylabel("frequency bin")
plt.title("frequency over time")
plt.colorbar(format="%+2.0f dB")
plt.show()
