"""
Live Meeting Summarizer Pro - Production Version
Processes real audio files with Whisper
Sends actual emails via SMTP
"""

import streamlit as st
import json
from datetime import datetime
import os
import base64

# Import our custom modules
try:
    from audio_processor import AudioProcessor, SpeakerDiarizer, SummaryGenerator
    from email_handler import EmailHandler
except:
    st.error("Error importing modules. Make sure audio_processor.py and email_handler.py exist.")

# ============= PAGE CONFIG =============
st.set_page_config(
    page_title="Live Meeting Summarizer",
    layout="wide",
    page_icon="🎤",
    initial_sidebar_state="expanded"
)

# ============= CUSTOM CSS - FIXED TEXT VISIBILITY =============
st.markdown("""
<style>
    /* CRITICAL: Force text visibility on all backgrounds */
    * {
        color: #ffffff !important;
    }
    
    body, .main, .stApp {
        background-color: #0e1117;
        color: #ffffff !important;
    }
    
    /* Text colors - FORCE WHITE/LIGHT */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    
    p, span, div, label {
        color: #c9d1
