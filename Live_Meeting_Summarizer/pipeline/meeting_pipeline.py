import os
import re
import logging
import torch
from transformers import pipeline
from stt.stt_manager import get_full_transcript

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- GLOBAL MODEL LOADING ---
# We use a global variable so we don't reload the model every time
summarizer = None

def load_model():
    global summarizer
    if summarizer is None:
        try:
            logger.info("Loading summarization model... (this happens only once)")
            device = 0 if torch.cuda.is_available() else -1
            # "sshleifer/distilbart-cnn-12-6" is faster and less prone to copying than full BART for short text
            summarizer = pipeline(
                "summarization", 
                model="sshleifer/distilbart-cnn-12-6", 
                device=device
            )
            logger.info("Summarization model loaded.")
        except Exception as e:
            logger.error(f"Failed to load global model: {e}")

# Load immediately on import
load_model()

def process_meeting(audio_file):
    """Process a meeting recording and return transcript and summary."""
    try:
        logger.info("Starting meeting processing...")
        
        # 1. Get transcript
        logger.info("Transcribing audio...")
        transcript = get_full_transcript(audio_file)
        
        if not transcript or not transcript.strip():
            return "", "Error: No speech detected or empty transcript"
            
        # 2. Generate summary
        logger.info("Generating summary...")
        summary = generate_summary(transcript)
        
        return transcript, summary
        
    except Exception as e:
        logger.error(f"Error processing meeting: {e}")
        return "", f"Error: {str(e)}"

def generate_summary(transcript):
    """
    Generate a summary.
    Includes logic to FORCE the model to rewrite text instead of copying.
    """
    # Fallback if model failed to load
    if summarizer is None:
        return _fallback_summary(transcript)

    try:
        input_word_count = len(transcript.split())
        logger.info(f"Input word count: {input_word_count}")

        # --- TUNING PARAMETERS ---
        
        # CASE 1: VERY SHORT TEXT (< 50 words)
        # It's hard to summarize 2 sentences. Just return them or a simple prefix.
        if input_word_count < 50:
            return transcript

        # CASE 2: SHORT/MEDIUM TEXT (50 - 300 words)
        # We need strict limits to force rewriting
        elif input_word_count < 300:
            max_len = 70
            min_len = 20
            # strict penalty to force rewriting
            ngram_limit = 3 
        
        # CASE 3: LONG TEXT (> 300 words)
        else:
            max_len = 200
            min_len = 60
            ngram_limit = 3

        # Prepare input
        # Adding a prefix helps hint the model
        input_text = "summarize: " + transcript

        # Run Summarizer
        summary_result = summarizer(
            input_text,
            max_length=max_len, 
            min_length=min_len, 
            do_sample=False, 
            
            # THIS IS THE KEY FIX:
            # Prevents copying any 3-word phrase exactly from the input.
            no_repeat_ngram_size=ngram_limit,
            
            # Penalizes length (encourages brevity)
            length_penalty=2.0,
            
            truncation=True
        )
        
        summary = summary_result[0]['summary_text']
        
        # Clean up: Sometimes it starts with punctuation
        summary = summary.strip()
        if summary.startswith(".") or summary.startswith(","):
            summary = summary[1:].strip()
            
        return summary

    except Exception as e:
        logger.warning(f"AI summarization failed: {str(e)}")
        return _fallback_summary(transcript)

def _fallback_summary(text):
    """Simple fallback if AI fails"""
    sentences = text.split('. ')
    return ". ".join(sentences[:2]) + "."