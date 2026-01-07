import sounddevice as sd
import numpy as np
import soundfile as sf
import os
import logging
from datetime import datetime
from config.settings import AUDIO_SETTINGS

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AudioRecorder:
    def __init__(self):
        # Use .get() to provide defaults if settings are missing
        self.sample_rate = AUDIO_SETTINGS.get('SAMPLE_RATE', 44100)
        self.channels = AUDIO_SETTINGS.get('CHANNELS', 1)
        self.recording = False
        self.frames = [] 
        self.stream = None

    def callback(self, indata, frames, time, status):
        """Threaded callback function to collect audio data."""
        if status:
            logger.warning(f"Audio callback status: {status}")
        if self.recording:
            self.frames.append(indata.copy())

    def start(self):
        """Starts the audio recording stream."""
        self.recording = True
        self.frames = []
        try:
            self.stream = sd.InputStream(
                samplerate=self.sample_rate,
                channels=self.channels,
                callback=self.callback,
                dtype='float32'
            )
            self.stream.start()
            logger.info("Recording started...")
        except Exception as e:
            self.recording = False
            logger.error(f"Failed to start recording: {e}")
            raise RuntimeError(f"Could not access microphone: {e}")

    def stop(self):
        """Stops the recording and closes the stream."""
        self.recording = False
        if self.stream:
            try:
                self.stream.stop()
                self.stream.close()
            except Exception as e:
                logger.error(f"Error closing stream: {e}")
            finally:
                self.stream = None
                logger.info("Recording stopped.")

        if not self.frames:
            return np.array([])
        
        # Concatenate all recorded frames into a single numpy array
        return np.concatenate(self.frames, axis=0)

    def save(self, audio_data, filename=None):
        """Saves the recorded audio data to a WAV file."""
        if len(audio_data) == 0:
            logger.warning("No audio data to save.")
            return None

        save_dir = AUDIO_SETTINGS.get('RECORDINGS_DIR', 'recordings')
        os.makedirs(save_dir, exist_ok=True)

        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.wav"
        
        filepath = os.path.join(save_dir, filename)
        
        # Save as 16-bit PCM WAV (standard for speech processing compatibility)
        sf.write(filepath, audio_data, self.sample_rate, subtype='PCM_16')
        logger.info(f"Audio saved to {filepath}")
        return filepath

# --- Helper Functions for Streamlit App ---

def start_recording():
    """Helper to create recorder instance and start."""
    recorder = AudioRecorder()
    recorder.start()
    return recorder

def stop_and_save(recorder_instance):
    """Helper to stop recorder and save file. Returns filepath."""
    if not recorder_instance:
        return None
    
    audio_data = recorder_instance.stop()
    return recorder_instance.save(audio_data)