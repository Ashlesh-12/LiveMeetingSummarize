import streamlit as st
import os
import json
import bcrypt
import time
from datetime import datetime
from audio.recorder import start_recording, stop_and_save
from pipeline.meeting_pipeline import process_meeting
from export.email_sender import send_summary_email
from export.pdf_export import save_meeting_pdf
from config.settings import AUDIO_SETTINGS, EMAIL_SETTINGS

# --- OPTIONAL IMPORTS (For Advanced Features) ---
try:
    from textblob import TextBlob
    HAS_TEXTBLOB = True
except ImportError:
    HAS_TEXTBLOB = False

# --- CONFIGURATION ---
USER_DB_FILE = "users.json"
RECORDINGS_DIR = AUDIO_SETTINGS.get('RECORDINGS_DIR', 'recordings')
os.makedirs('exports', exist_ok=True)
os.makedirs(RECORDINGS_DIR, exist_ok=True)

st.set_page_config(
    page_title="Meeting AI Pro", 
    page_icon="🎙️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .recording-box {
        background-color: #ff4b4b;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        animation: pulse 2s infinite;
        margin-bottom: 20px;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(255, 75, 75, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0); }
    }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; font-weight: 600; }
    
    /* Chat Bubble Styling */
    .user-msg { background-color: #2b313e; padding: 10px; border-radius: 10px; margin: 5px 0; text-align: right; }
    .ai-msg { background-color: #1f2937; padding: 10px; border-radius: 10px; margin: 5px 0; border-left: 4px solid #00c0f2; }
    </style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---

def extract_action_items(text):
    """Heuristic-based action item extraction."""
    action_keywords = ["todo", "to do", "action", "deadline", "assign", "schedule", "will", "must", "plan"]
    sentences = text.split('.')
    actions = [s.strip() for s in sentences if any(k in s.lower() for k in action_keywords) and len(s.split()) > 3]
    return actions

def get_sentiment(text):
    """Calculate sentiment polarity."""
    if not HAS_TEXTBLOB: return 0, "Neutral"
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    if score > 0.1: return score, "Positive"
    elif score < -0.1: return score, "Negative"
    return score, "Neutral"

# --- AUTHENTICATION LOGIC ---

def load_users():
    if not os.path.exists(USER_DB_FILE): return {}
    try:
        with open(USER_DB_FILE, "r") as f: return json.load(f)
    except: return {}

def save_users(users):
    with open(USER_DB_FILE, "w") as f: json.dump(users, f)

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🔒 Access Meeting AI")
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
                    if new_user in users: st.warning("Username exists.")
                    elif len(new_pass) < 4: st.warning("Password too short.")
                    else:
                        users[new_user] = hash_password(new_pass)
                        save_users(users)
                        st.success("Account created! Please log in.")

# --- MAIN APP LOGIC ---

def get_recordings():
    try:
        files = [f for f in os.listdir(RECORDINGS_DIR) if f.endswith('.wav')]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(RECORDINGS_DIR, x)), reverse=True)
        return files
    except: return []

def main():
    if 'authenticated' not in st.session_state: st.session_state.authenticated = False
    if not st.session_state.authenticated:
        login_page()
        return

    # Initialize Session Vars
    defaults = {'recorder': None, 'recording': False, 'transcript': "", 
                'summary': "", 'audio_file': None, 'chat_history': []}
    for k, v in defaults.items():
        if k not in st.session_state: st.session_state[k] = v

    # --- SIDEBAR ---
    with st.sidebar:
        st.title(f"👤 {st.session_state.username}")
        if st.button("🔒 Logout"):
            st.session_state.authenticated = False
            st.rerun()
            
        st.divider()
        st.subheader("📂 Library & Upload")
        
        # 1. FILE UPLOAD (New Feature)
        uploaded_file = st.file_uploader("Upload Audio", type=['wav', 'mp3'])
        if uploaded_file and st.button("▶️ Process Upload"):
            file_path = os.path.join(RECORDINGS_DIR, uploaded_file.name)
            with open(file_path, "wb") as f: f.write(uploaded_file.getbuffer())
            st.session_state.audio_file = file_path
            with st.spinner("Processing..."):
                st.session_state.transcript, st.session_state.summary = process_meeting(file_path)
            st.rerun()

        # 2. EXISTING RECORDINGS
        saved_files = get_recordings()
        if saved_files:
            selected_file = st.selectbox("Past Recordings", saved_files)
            if st.button("🔄 Reload File"):
                file_path = os.path.join(RECORDINGS_DIR, selected_file)
                st.session_state.audio_file = file_path
                with st.spinner("Processing..."):
                    st.session_state.transcript, st.session_state.summary = process_meeting(file_path)
                st.rerun()
            
        st.divider()
        if st.session_state.transcript and st.button("📄 Save PDF"):
            fname = f"exports/summary_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
            if save_meeting_pdf(st.session_state.transcript, st.session_state.summary, fname, "Summary"):
                st.success(f"Saved: {fname}")

    # --- MAIN UI ---
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🎙️ Meeting AI Pro")
        st.caption("Live Transcription, Summarization & Analytics")
    with col2:
        if st.session_state.recording:
            st.markdown('<div class="recording-box">🔴 REC</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Controls
    if not st.session_state.recording:
        if st.button("🎤 Start Recording", type="primary"):
            st.session_state.recorder = start_recording()
            st.session_state.recording = True
            st.rerun()
    else:
        if st.button("⏹️ Stop & Process", type="primary"):
            st.session_state.audio_file = stop_and_save(st.session_state.recorder)
            st.session_state.recording = False
            with st.status("Processing..."):
                st.session_state.transcript, st.session_state.summary = process_meeting(st.session_state.audio_file)
            st.rerun()

    # Results Section
    if st.session_state.transcript:
        # Create 4 Tabs for Advanced Features
        tab1, tab2, tab3, tab4 = st.tabs(["📝 Summary", "✅ Actions", "📊 Analysis", "💬 Chat"])
        
        with tab1:
            st.subheader("Executive Summary")
            st.text_area("Summary", st.session_state.summary, height=300)
            
        with tab2:
            st.subheader("Detected Action Items")
            actions = extract_action_items(st.session_state.transcript)
            if actions:
                for i, action in enumerate(actions, 1):
                    st.info(f"**{i}.** {action}")
            else:
                st.write("No clear action items detected.")
                
        with tab3:
            st.subheader("Meeting Analytics")
            col_a, col_b = st.columns(2)
            
            # Word Count
            word_count = len(st.session_state.transcript.split())
            col_a.metric("Total Words", word_count)
            
            # Sentiment Analysis
            score, label = get_sentiment(st.session_state.transcript)
            col_b.metric("Sentiment", label, f"{score:.2f}")
            
            if not HAS_TEXTBLOB:
                st.warning("Install 'textblob' for detailed sentiment analysis.")
            
        with tab4:
            st.subheader("Chat with Transcript")
            user_query = st.text_input("Ask a question about the meeting:")
            if user_query:
                # Simple Context Search (Contextual)
                results = []
                sentences = st.session_state.transcript.split('.')
                for s in sentences:
                    if any(word in s.lower() for word in user_query.lower().split()):
                        results.append(s.strip())
                
                if results:
                    response = "Here is what I found:\n" + "...\n".join(results[:3])
                else:
                    response = "I couldn't find specific mentions of that in the transcript."
                    
                st.markdown(f'<div class="user-msg">👤 {user_query}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="ai-msg">🤖 {response}</div>', unsafe_allow_html=True)
                
    else:
        if not st.session_state.recording:
            st.info("👋 Ready! Upload a file or start recording.")

if __name__ == "__main__":
    main()