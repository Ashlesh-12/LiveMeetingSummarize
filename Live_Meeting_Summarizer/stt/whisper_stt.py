# stt/whisper_stt.py
import torch
import numpy as np
import logging
from config.settings import WHISPER_SETTINGS

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global model variable
_model = None

def load_model():
    """Load Whisper model with caching."""
    global _model
    if _model is None:
        try:
            import whisper
            logger.info("Loading Whisper %s model on %s...", WHISPER_SETTINGS['MODEL_SIZE'], WHISPER_SETTINGS['DEVICE'])
            _model = whisper.load_model(WHISPER_SETTINGS['MODEL_SIZE'], device=WHISPER_SETTINGS['DEVICE'])
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error("Failed to load Whisper model: %s", e)
            _model = None
    return _model

def transcribe(audio_np, language="en"):
    """Transcribe audio using Whisper."""
    try:
        logger.info("Starting transcription...")
        model = load_model()
        if model is None:
            return ""
        
        # Convert audio to float32 if needed
        if audio_np.dtype != np.float32:
            audio_np = audio_np.astype(np.float32)
            
        # Transcribe with anti-hallucination flags:
        # - condition_on_previous_text=False  → prevents decoder looping on clean/TTS audio
        # - no_speech_threshold               → skip segments that look like silence
        # - compression_ratio_threshold       → skip segments with suspiciously high repetition
        result = model.transcribe(
            audio_np,
            language=language,
            fp16=torch.cuda.is_available(),
            temperature=0.0,                    # greedy decoding – fast & deterministic
            condition_on_previous_text=False,   # KEY: stops repetition hallucinations
            no_speech_threshold=0.6,
            compression_ratio_threshold=2.4,
            initial_prompt="This is a business meeting recording."
        )
        
        transcript = result.get("text", "").strip()
        logger.info(f"Transcription complete. Length: {len(transcript)} characters")
        
        if not transcript:
            logger.warning("Whisper returned an empty transcription")
            
        return transcript
        
    except Exception as e:
        logger.error(f"Error in transcription: {e}")
        return ""
