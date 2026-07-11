import re
import math
import logging
import collections
from stt.stt_manager import get_full_transcript

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def process_meeting(audio_file):
    """Process a meeting recording and return transcript and summary."""
    try:
        logger.info("Starting meeting processing...")

        # 1. Transcribe
        logger.info("Transcribing audio...")
        transcript = get_full_transcript(audio_file)

        if not transcript or not transcript.strip():
            return "", "Error: No speech detected or empty transcript"

        # 2. Summarise
        logger.info("Generating summary...")
        summary = generate_summary(transcript)

        return transcript, summary

    except Exception as e:
        logger.error("Error processing meeting: %s", e)
        return "", f"Error: {str(e)}"


def generate_summary(transcript: str) -> str:
    """
    Generate a structured meeting summary using extractive NLP.
    No neural model required — works within Streamlit Cloud's 1 GB RAM limit.

    Returns a multi-section markdown string:
        **Meeting Overview**
        **Key Discussion Points**
        **Action Items & Decisions**
    """
    try:
        word_count = len(transcript.split())

        if word_count < 20:
            return transcript.strip()

        sentences = _split_sentences(transcript)

        if len(sentences) <= 3:
            return transcript.strip()

        # ---- TF-IDF sentence scoring ----------------------------------------
        scores = _tfidf_sentence_scores(sentences)

        # ---- How many sentences to select -----------------------------------
        # Roughly: 1 sentence per 40 words of input, min 3, max 12
        n_select = max(3, min(12, word_count // 40))

        ranked = sorted(range(len(sentences)), key=lambda i: scores[i], reverse=True)
        top_indices = set(ranked[:n_select])

        # Chronological order → maintain dialogue flow
        top_sentences = [sentences[i] for i in sorted(top_indices)]

        # ---- Structured output ---------------------------------------------
        overview_sents    = top_sentences[:max(1, len(top_sentences) // 3)]
        remaining_sents   = top_sentences[len(overview_sents):]

        action_keywords   = _action_item_sentences(sentences)
        key_points        = [s for s in remaining_sents if s not in action_keywords]

        sections = []

        # Overview
        overview_text = " ".join(overview_sents)
        sections.append(f"**📋 Meeting Overview**\n{overview_text}")

        # Key points
        if key_points:
            bullet_points = "\n".join(f"• {s}" for s in key_points)
            sections.append(f"**🔑 Key Discussion Points**\n{bullet_points}")

        # Action items
        if action_keywords:
            bullet_actions = "\n".join(f"• {s}" for s in action_keywords[:6])
            sections.append(f"**✅ Action Items & Decisions**\n{bullet_actions}")

        return "\n\n".join(sections)

    except Exception as e:
        logger.warning("Summarisation error: %s", e)
        return _fallback_summary(transcript)


# ---------------------------------------------------------------------------
# Helper utilities (also used by unit tests)
# ---------------------------------------------------------------------------

def _split_sentences(text: str):
    """Split text into clean sentences."""
    raw = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in raw if len(s.strip()) > 10]


def _tfidf_sentence_scores(sentences):
    """
    Score every sentence with a TF-IDF-inspired weight.
    Returns a list of float scores aligned to `sentences`.
    """
    STOP_WORDS = {
        "the", "and", "a", "of", "to", "is", "in", "it", "that", "i", "you",
        "he", "she", "we", "they", "this", "but", "on", "are", "for", "with",
        "was", "as", "at", "by", "an", "be", "my", "me", "our", "us", "your",
        "them", "have", "has", "had", "do", "does", "did", "so", "then", "there",
        "what", "where", "when", "why", "how", "all", "any", "both", "each",
        "from", "or", "not", "no", "its", "if", "just", "about", "up", "out",
        "also", "been", "more", "will", "would", "could", "should", "can",
        "very", "well", "some", "one", "two", "three", "four", "five", "said",
        "like", "know", "get", "got", "go", "going", "think", "um", "uh", "okay",
        "yeah", "yes", "no", "right", "sure", "actually", "basically", "really",
    }

    n = len(sentences)
    if n == 0:
        return []

    # Term frequency per sentence
    tokenized = []
    for s in sentences:
        words = [w for w in re.findall(r'\b[a-z]{3,}\b', s.lower()) if w not in STOP_WORDS]
        tokenized.append(words)

    # Document frequency (how many sentences contain a word)
    df = collections.Counter()
    for words in tokenized:
        df.update(set(words))

    scores = []
    for i, words in enumerate(tokenized):
        if not words:
            scores.append(0.0)
            continue
        tf = collections.Counter(words)
        score = 0.0
        for w, count in tf.items():
            idf = math.log((n + 1) / (df[w] + 1))
            score += (count / len(words)) * idf
        # Slight position bias: first quarter of doc gets +10%
        if i < n // 4:
            score *= 1.10
        scores.append(score)

    return scores


def _action_item_sentences(sentences):
    """
    Identify sentences that sound like action items or decisions.
    Returns them in chronological order.
    """
    ACTION_PATTERNS = [
        r'\bwill\b', r'\bshould\b', r'\bneed to\b', r'\bgoing to\b',
        r'\baction\b', r'\btask\b', r'\bfollow.?up\b', r'\bdeadline\b',
        r'\bby (monday|tuesday|wednesday|thursday|friday|next week|tomorrow|end of)\b',
        r'\bdecided\b', r'\bagreed\b', r'\bresponsible\b', r'\bassigned\b',
        r'\bmake sure\b', r'\bensure\b', r'\bplease\b', r'\bcommit\b',
        r'\bschedule\b', r'\bsend\b', r'\bshare\b', r'\bprepare\b',
        r'\bcreate\b', r'\bbuild\b', r'\bdeliver\b', r'\breview\b',
    ]
    combined = re.compile('|'.join(ACTION_PATTERNS), re.IGNORECASE)
    return [s for s in sentences if combined.search(s)]


def _fallback_summary(text: str) -> str:
    """
    Ultra-simple fallback: return first few sentences.
    Called only if everything else fails.
    """
    sentences = _split_sentences(text)
    return " ".join(sentences[:4]) if sentences else text[:500]


def _chunk_text(text: str, chunk_size: int = 650):
    """Split text into word-count chunks (used by unit tests)."""
    words = text.split()
    if not words:
        return []
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
