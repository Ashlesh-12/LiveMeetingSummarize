import re
import logging
import torch
from transformers import pipeline
from stt.stt_manager import get_full_transcript

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

summarizer = None

def load_model():
    global summarizer
    if summarizer is not None:
        return summarizer

    try:
        logger.info("Loading summarization model...")
        device = 0 if torch.cuda.is_available() else -1
        # DistilBART is a good speed/quality tradeoff for meeting notes.
        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            device=device
        )
        logger.info("Summarization model loaded.")
    except Exception as e:
        logger.error("Failed to load summarization model: %s", e)
        summarizer = None
    return summarizer

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
    try:
        input_word_count = len(transcript.split())
        logger.info(f"Input word count: {input_word_count}")

        # --- TUNING PARAMETERS ---
        
        # CASE 1: VERY SHORT TEXT (< 50 words)
        # It's hard to summarize 2 sentences. Just return them or a simple prefix.
        if input_word_count < 50:
            return transcript

        # Load model only when summarization is actually needed.
        model = load_model()
        if model is None:
            return _fallback_summary(transcript)

        if input_word_count < 300:
            max_len = 90
            min_len = 20
            summary = _summarize_chunk(model, transcript, max_len=max_len, min_len=min_len)
        else:
            # Chunk very long transcripts to avoid truncation at model token limits.
            chunks = _chunk_text(transcript, chunk_size=650)
            chunk_summaries = []
            for idx, chunk in enumerate(chunks, 1):
                logger.info("Summarizing chunk %s/%s", idx, len(chunks))
                chunk_summaries.append(_summarize_chunk(model, chunk, max_len=120, min_len=35))
            combined = " ".join(chunk_summaries)
            summary = _summarize_chunk(model, combined, max_len=180, min_len=60)
        
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
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    if not sentences:
        return "No summary available."
    return " ".join(sentences[:3])

def _chunk_text(text, chunk_size=650):
    words = text.split()
    if not words:
        return []
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def _summarize_chunk(model, text, max_len, min_len):
    input_text = "summarize: " + text
    result = model(
        input_text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False,
        no_repeat_ngram_size=3,
        length_penalty=2.0,
        truncation=True
    )
    return result[0]["summary_text"].strip()
