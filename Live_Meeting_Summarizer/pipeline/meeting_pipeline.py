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
        # t5-small is a very light model (~240MB) suitable for Streamlit Cloud constraints.
        summarizer = pipeline(
            "summarization",
            model="t5-small",
            device=device,
            framework="pt",   # force PyTorch
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
    """
    Extractive sentence frequency ranking summarizer.
    Scores sentences based on word frequencies of non-stop-words.
    Selects top 4 chronological sentences to build a high-quality summary.
    """
    try:
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
        if len(sentences) <= 4:
            return text

        # 1. Compute word frequencies
        word_frequencies = {}
        stop_words = {
            "the", "and", "a", "of", "to", "is", "in", "it", "that", "i", "you",
            "he", "she", "we", "they", "this", "but", "on", "are", "for", "with",
            "was", "as", "at", "by", "an", "be", "my", "me", "our", "us", "your",
            "them", "have", "has", "had", "do", "does", "did", "so", "then", "there",
            "what", "where", "when", "why", "how", "all", "any", "both", "each"
        }
        words = re.findall(r'\b\w+\b', text.lower())
        for word in words:
            if word not in stop_words:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1

        if not word_frequencies:
            return " ".join(sentences[:4])

        # Normalize frequencies
        max_freq = max(word_frequencies.values())
        for word in word_frequencies:
            word_frequencies[word] /= max_freq

        # 2. Score sentences
        sentence_scores = {}
        for sent in sentences:
            score = 0
            sent_words = re.findall(r'\b\w+\b', sent.lower())
            for word in sent_words:
                if word in word_frequencies:
                    score += word_frequencies[word]
            # Normalize score by length to avoid bias towards long run-on sentences
            sentence_scores[sent] = score / max(1, len(sent_words))

        # 3. Sort sentences by score and take top 4
        sorted_sentences = sorted(sentence_scores.keys(), key=lambda x: sentence_scores[x], reverse=True)
        top_sentences = sorted_sentences[:4]

        # 4. Re-order chronologically to maintain dialogue flow
        summary_sentences = [s for s in sentences if s in top_sentences]
        return " ".join(summary_sentences)
    except Exception:
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
