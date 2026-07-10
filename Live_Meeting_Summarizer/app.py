import base64
import json
import logging
import os
from datetime import datetime
from pathlib import Path

import bcrypt
import streamlit as st

from audio_recorder_streamlit import audio_recorder
from config.settings import AUDIO_SETTINGS
from export.pdf_export import save_meeting_pdf
from pipeline.meeting_pipeline import process_meeting

# --- OPTIONAL IMPORTS (Advanced Features) ---
try:
    from textblob import TextBlob

    HAS_TEXTBLOB = True
except ImportError:
    HAS_TEXTBLOB = False

# --- CONFIGURATION ---
USER_DB_FILE = "users.json"
RECORDINGS_DIR = AUDIO_SETTINGS.get("RECORDINGS_DIR", "recordings")
os.makedirs("exports", exist_ok=True)
os.makedirs(RECORDINGS_DIR, exist_ok=True)
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="Meeting AI Pro",
    page_icon="M",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CSS STYLING ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@300;400;500;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Force main application backgrounds to be dark slate/navy */
    .stApp, [data-testid="stAppViewContainer"], .main {
        background-color: #0b0f19 !important;
        color: #f3f4f6 !important;
    }
    
    /* Style top header bar to dark color */
    header[data-testid="stHeader"] {
        background-color: #0b0f19 !important;
        border-bottom: 1px solid #181f33 !important;
    }
    
    /* Gradient Title */
    .gradient-title {
        background: linear-gradient(135deg, #00c0f2 0%, #8a2be2 50%, #ff4b4b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Outfit', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin-bottom: 0.1rem;
    }
    
    /* Sidebar polish */
    section[data-testid="stSidebar"] {
        background-color: #080b13 !important;
        border-right: 1px solid #181f33;
    }
    
    /* Rounded Cards for Metrics */
    div[data-testid="stMetric"] {
        background-color: #121826;
        border: 1px solid #1e2640;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: #00c0f2;
        box-shadow: 0 8px 24px rgba(0, 192, 242, 0.15);
    }
    
    /* Premium Streamlit Buttons styling */
    .stButton>button {
        border-radius: 12px !important;
        font-weight: 600 !important;
        height: 3.2em !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    /* Primary buttons (vibrant cyan-purple gradient) */
    button[data-testid="stBaseButton-primary"] {
        background: linear-gradient(135deg, #00c0f2 0%, #8a2be2 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 192, 242, 0.25) !important;
    }
    button[data-testid="stBaseButton-primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(138, 43, 226, 0.45) !important;
        background: linear-gradient(135deg, #00d6ff 0%, #9d3eff 100%) !important;
    }
    
    /* Secondary buttons (subtle dark glass card) */
    button[data-testid="stBaseButton-secondary"] {
        background-color: #121826 !important;
        border: 1px solid #1e2640 !important;
        color: #f3f4f6 !important;
    }
    button[data-testid="stBaseButton-secondary"]:hover {
        border-color: #00c0f2 !important;
        box-shadow: 0 4px 15px rgba(0, 192, 242, 0.15) !important;
        transform: translateY(-2px);
    }
    
    /* Polish default headers */
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    .user-msg { background-color: #2b313e; color: #ffffff; padding: 10px; border-radius: 10px; margin: 5px 0; text-align: right; }
    .ai-msg { background-color: #1f2937; color: #ffffff; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #00c0f2; }
    
    /* Dark mode file uploader card overrides */
    div[data-testid="stFileUploader"] {
        background-color: #121826 !important;
        border: 1px dashed #1e2640 !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    div[data-testid="stFileUploader"] section {
        background-color: #121826 !important;
        color: #f3f4f6 !important;
    }
    div[data-testid="stFileUploader"] label {
        color: #94a3b8 !important;
    }
    div[data-testid="stFileUploader"] button {
        background-color: #1a2238 !important;
        color: #f3f4f6 !important;
        border: 1px solid #2a3556 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stFileUploader"] button:hover {
        border-color: #00c0f2 !important;
        background-color: #232d4b !important;
    }
    
    /* Dark mode select boxes override */
    div[data-baseweb="select"] > div {
        background-color: #121826 !important;
        border-color: #1e2640 !important;
        color: #f3f4f6 !important;
    }
    
    /* Info alert notification style override */
    div[data-testid="stNotification"] {
        background-color: #121826 !important;
        border: 1px solid #1e2640 !important;
        border-radius: 12px !important;
    }
    div[data-testid="stNotification"] div {
        color: #00c0f2 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# --- HELPER FUNCTIONS ---
def _pdf_download_link(pdf_bytes: bytes, filename: str, label: str = "Download PDF Report") -> str:
    """Return an HTML anchor tag that triggers a direct browser download with the correct filename."""
    b64 = base64.b64encode(pdf_bytes).decode()
    return (
        f'<a href="data:application/pdf;base64,{b64}" '
        f'download="{filename}" '
        f'style="display:inline-block;padding:10px 22px;background:linear-gradient(135deg,#00c0f2,#8a2be2);'
        f'color:#fff;font-weight:600;border-radius:8px;text-decoration:none;font-size:14px;'
        f'box-shadow:0 4px 15px rgba(0,192,242,0.3);transition:all 0.2s;">'
        f'{label}</a>'
    )


def extract_action_items(text):
    """Heuristic-based action item extraction."""
    action_keywords = ["todo", "to do", "action", "deadline", "assign", "schedule", "will", "must", "plan"]
    sentences = text.split(".")
    actions = [s.strip() for s in sentences if any(k in s.lower() for k in action_keywords) and len(s.split()) > 3]
    return actions


def get_sentiment(text):
    """Calculate sentiment polarity."""
    if not HAS_TEXTBLOB:
        return 0, "Neutral"
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    if score > 0.1:
        return score, "Positive"
    if score < -0.1:
        return score, "Negative"
    return score, "Neutral"


def _safe_uploaded_filename(filename):
    """Normalize upload filename and avoid unsafe names/collisions."""
    base_name = Path(filename).name
    stem, ext = os.path.splitext(base_name)
    safe_stem = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in stem).strip("_")
    if not safe_stem:
        safe_stem = "uploaded_audio"
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{safe_stem}_{ts}{ext.lower()}"


def _process_audio_file(file_path):
    st.session_state.audio_file = file_path
    st.session_state.current_audio_file = file_path  # track for PDF report
    with st.spinner("Processing..."):
        transcript, summary = process_meeting(file_path)

    if summary.startswith("Error:"):
        st.error(summary)
        st.session_state.transcript = ""
        st.session_state.summary = ""
        logger.warning("Processing failed for %s: %s", file_path, summary)
        return

    st.session_state.transcript = transcript
    st.session_state.summary = summary


# --- AUTHENTICATION LOGIC ---
def load_users():
    if not os.path.exists(USER_DB_FILE):
        return {}
    try:
        with open(USER_DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_users(users):
    with open(USER_DB_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f)


def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def check_password(password, hashed):
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False


def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="gradient-title" style="font-size: 2.2rem; text-align: center;">Access Meeting AI</div>', unsafe_allow_html=True)
        tab_login, tab_signup = st.tabs(["Login", "Create Account"])

        with tab_login:
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.form_submit_button("Log In", type="primary"):
                    users = load_users()
                    if username in users and check_password(password, users[username]):
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")

        with tab_signup:
            with st.form("signup_form"):
                new_user = st.text_input("Choose Username")
                new_pass = st.text_input("Choose Password", type="password")
                if st.form_submit_button("Sign Up"):
                    users = load_users()
                    if new_user in users:
                        st.warning("Username exists.")
                    elif len(new_pass) < 4:
                        st.warning("Password too short.")
                    else:
                        users[new_user] = hash_password(new_pass)
                        save_users(users)
                        st.success("Account created. Please log in.")


# --- MAIN APP LOGIC ---
def get_recordings():
    try:
        files = [f for f in os.listdir(RECORDINGS_DIR) if f.lower().endswith((".wav", ".mp3", ".m4a", ".flac"))]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(RECORDINGS_DIR, x)), reverse=True)
        return files
    except Exception:
        return []


def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if not st.session_state.authenticated:
        login_page()
        return

    defaults = {
        "transcript": "",
        "summary": "",
        "audio_file": None,
        "chat_history": [],
        "pdf_bytes": None,
        "pdf_filename": "",
        "current_audio_file": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    with st.sidebar:
        st.title(f"User: {st.session_state.username}")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

        st.divider()
        st.subheader("Library and Upload")

        uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a", "flac"])
        if uploaded_file and st.button("Process Upload"):
            safe_name = _safe_uploaded_filename(uploaded_file.name)
            file_path = os.path.join(RECORDINGS_DIR, safe_name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            _process_audio_file(file_path)
            st.rerun()

        saved_files = get_recordings()
        if saved_files:
            selected_file = st.selectbox("Past Recordings", saved_files)
            if st.button("Reload File"):
                file_path = os.path.join(RECORDINGS_DIR, selected_file)
                _process_audio_file(file_path)
                st.rerun()

        st.divider()
        if st.session_state.transcript:
            if st.button("Save & Download PDF Report"):
                actions = extract_action_items(st.session_state.transcript)
                audio_name = st.session_state.get("current_audio_file", "") or ""
                fname = f"exports/summary_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
                ok = save_meeting_pdf(
                    transcript=st.session_state.transcript,
                    summary=st.session_state.summary,
                    filepath=fname,
                    title="Meeting Intelligence Report",
                    action_items=actions,
                    username=st.session_state.get("username", "N/A"),
                    audio_filename=os.path.basename(audio_name) if audio_name else "N/A",
                )
                if ok:
                    # Store PDF bytes in session_state so link survives reruns
                    with open(fname, "rb") as f:
                        st.session_state.pdf_bytes    = f.read()
                        st.session_state.pdf_filename = os.path.basename(fname)
                    st.success("Report generated! Click the link below to download.")

            # Render a reliable base64 HTML download link (avoids Streamlit UUID bug)
            if st.session_state.get("pdf_bytes"):
                link_html = _pdf_download_link(
                    st.session_state.pdf_bytes,
                    st.session_state.pdf_filename,
                )
                st.markdown(link_html, unsafe_allow_html=True)


    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div class="gradient-title">Meeting AI Pro</div>', unsafe_allow_html=True)
        st.caption("Live transcription, summarization, and analytics")
    with col2:
        pass

    st.divider()

    st.write("### Record Live Meeting")
    st.caption("Click the microphone button to start recording from your browser. Click it again to stop and process.")
    audio_bytes = audio_recorder(
        text="",
        recording_color="#ff4b4b",
        neutral_color="#6c757d",
        icon_name="microphone",
        icon_size="2x"
    )
    
    if audio_bytes:
        audio_len = len(audio_bytes)
        if "last_recorded_len" not in st.session_state or st.session_state.last_recorded_len != audio_len:
            st.session_state.last_recorded_len = audio_len
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"recording_{timestamp}.wav"
            file_path = os.path.join(RECORDINGS_DIR, file_name)
            try:
                with open(file_path, "wb") as f:
                    f.write(audio_bytes)
                _process_audio_file(file_path)
                st.rerun()
            except Exception as e:
                st.error(f"Error saving recorded audio: {e}")

    if st.session_state.transcript:
        tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Actions", "Analysis", "Chat"])

        with tab1:
            st.subheader("Executive Summary")
            st.text_area("Summary", st.session_state.summary, height=300)

        with tab2:
            st.subheader("Detected Action Items")
            actions = extract_action_items(st.session_state.transcript)
            if actions:
                for idx, action in enumerate(actions, 1):
                    st.info(f"**{idx}.** {action}")
            else:
                st.write("No clear action items detected.")

        with tab3:
            st.subheader("Meeting Analytics")
            col_a, col_b = st.columns(2)

            word_count = len(st.session_state.transcript.split())
            col_a.metric("Total Words", word_count)

            score, label = get_sentiment(st.session_state.transcript)
            col_b.metric("Sentiment", label, f"{score:.2f}")

            if not HAS_TEXTBLOB:
                st.warning("Install 'textblob' for detailed sentiment analysis.")

        with tab4:
            # Subheader with a Clear button
            col_chat_title, col_chat_clear = st.columns([3, 1])
            col_chat_title.subheader("Chat with Transcript")
            if col_chat_clear.button("Clear Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
                
            # Scrollable chat messages container
            chat_container = st.container()
            with chat_container:
                if not st.session_state.chat_history:
                    st.info("Ask questions about this meeting. I'll search the transcript and answer.")
                else:
                    for role, text in st.session_state.chat_history:
                        with st.chat_message(role):
                            st.write(text)

            # Chat input widget
            user_query = st.chat_input("Ask a question about the meeting:")
            if user_query:
                # Add to history immediately so user sees it
                st.session_state.chat_history.append(("user", user_query))
                
                # Perform keyword ranking search
                import re
                STOP_WORDS = {
                    "the", "a", "an", "and", "or", "but", "if", "then", "else", "is", "are", 
                    "was", "were", "be", "been", "being", "to", "of", "in", "on", "at", "for", 
                    "with", "about", "here", "there", "when", "where", "why", "how", "all", 
                    "any", "both", "each", "other", "some", "no", "not", "only", "so", "than", 
                    "too", "very", "can", "will", "just", "should", "now", "what", "who", 
                    "which", "this", "that", "these", "those", "i", "you", "he", "she", 
                    "it", "we", "they", "me", "him", "her", "us", "them", "my", "your", 
                    "his", "its", "our", "their"
                }
                
                query_words = [w.strip("?,.!") for w in user_query.lower().split()]
                keywords = [w for w in query_words if w and w not in STOP_WORDS]
                
                if not keywords:
                    keywords = [w for w in query_words if w]
                    
                sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", st.session_state.transcript) if s.strip()]
                
                scored_sentences = []
                for sentence in sentences:
                    sentence_words = set(w.strip("?,.!") for w in sentence.lower().split())
                    score = sum(1 for kw in keywords if kw in sentence_words)
                    if score > 0:
                        scored_sentences.append((score, sentence))
                        
                scored_sentences.sort(key=lambda x: x[0], reverse=True)
                results = [sentence for score, sentence in scored_sentences]

                if results:
                    response = "Here is what I found:\n\n" + "\n\n...\n\n".join(results[:3])
                else:
                    response = "I couldn't find specific mentions of that in the transcript."
                    
                st.session_state.chat_history.append(("assistant", response))
                st.rerun()
    else:
        st.info("Ready. Upload a file or record audio.")


if __name__ == "__main__":
    main()
