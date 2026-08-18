---
title: Meeting AI Pro
emoji: 🎙️
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
pinned: false
license: mit
short_description: Live meeting transcription, AI summarization & analytics
---

# Meeting AI Pro 🎙️

🚀 **Live App:** [https://meeting-ai-pro.streamlit.app/](https://meeting-ai-pro.streamlit.app/)

> **Live transcription · AI summarization · Action items · Sentiment analytics · PDF reports**

A full-stack AI meeting assistant built with OpenAI Whisper (speech-to-text), DistilBART (summarization), and Streamlit.

## Features
- 🎤 **Browser-based mic recording** — record directly from your browser, no install needed
- 📁 **Audio file upload** — WAV, MP3, M4A, FLAC
- 📝 **Whisper STT** — fast, accurate transcription (base model, CPU)
- 🤖 **AI Summary** — DistilBART extracts the key points
- ✅ **Action Items** — heuristic extraction of tasks and deadlines
- 📊 **Sentiment Analysis** — polarity & subjectivity via TextBlob
- 📄 **Full PDF Report** — 2-page professional report with all sections
- 💬 **Chat with Transcript** — ask questions about the meeting

## Default Login
| Username | Password |
|---|---|
| `demo` | `demo1234` |

Use **Register** to create your own account.

## Running Locally

If you clone or download this repository to run it on your own machine, follow these steps:

1. **Open a terminal** and navigate into the project folder:
   ```bash
   cd Live_Meeting_Summarizer
   ```
2. **Install the required dependencies** (a virtual environment is recommended):
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
4. The app will automatically open in your web browser at `http://localhost:8501`.
