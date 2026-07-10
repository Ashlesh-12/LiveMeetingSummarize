# Live Meeting Summarizer

An end-to-end Streamlit application that records or uploads meeting audio, transcribes speech with Whisper, summarizes discussion using a transformer model, extracts action items, and exports a PDF report.

## 1) Design Approach

The project follows a pragmatic pipeline architecture:

1. Capture audio (live recording or uploaded file).
2. Normalize audio for speech-to-text.
3. Transcribe speech to text with Whisper.
4. Summarize transcript with a transformer summarizer.
5. Generate analytics (sentiment, word count, action items).
6. Export summary/transcript to PDF.

Engineering priorities used in this implementation:

- Reliability first: graceful handling when model/microphone/audio parsing fails.
- Predictable UX: one processing path for upload, reload, and recording.
- Scalability for long meetings: chunked summarization to avoid truncation.
- Maintainability: clear separation between UI, pipeline, STT, and export modules.

## 2) Technology Stack

- UI: Streamlit
- Audio capture: sounddevice, soundfile
- Audio loading/resampling: soundfile + librosa
- Speech-to-text: openai-whisper
- Summarization: Hugging Face transformers (`sshleifer/distilbart-cnn-12-6`)
- PDF export: fpdf2
- Authentication: bcrypt with local `users.json`
- Config/env: python-dotenv
- Optional NLP sentiment: TextBlob

## 3) Project Structure

```text
app.py                      # Streamlit UI + interaction logic
config/settings.py          # Environment and runtime settings
audio/recorder.py           # Live microphone recording
stt/stt_manager.py          # Audio decoding + transcription orchestration
stt/whisper_stt.py          # Whisper model loading + transcription
pipeline/meeting_pipeline.py# End-to-end transcript -> summary pipeline
export/pdf_export.py        # PDF report generation
export/email_sender.py      # Email utility (optional feature)
tests/                      # Automated smoke/unit tests
docs/health_check.py        # Interview/demo health script
```

## 4) Implementation Highlights

- Lazy model loading for summarizer and Whisper to reduce startup overhead.
- Defensive error propagation so failures return clean user-facing messages.
- Safe upload file naming to avoid path issues and accidental collisions.
- Long transcript chunking and re-summarization to preserve more context.
- Automated tests for critical helper behavior and PDF generation.

## 5) Setup and Run

### Prerequisites

- Python 3.10+ (tested on Python 3.11)
- Microphone permissions (for live recording)

### Install

```powershell
python -m pip install -r requirements.txt
```

### Start app

```powershell
streamlit run app.py
```

### Run tests

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

### Run health check

```powershell
python docs/health_check.py
```

## 6) Interview Demo Flow (5-7 min)

1. Login/Create account.
2. Upload a short audio file (faster than live recording for demo).
3. Show transcript and generated summary.
4. Open Actions and Analysis tabs.
5. Export PDF and open generated file from `exports/`.
6. Mention tests and health check for engineering quality.

## 7) Challenges and How They Were Solved

- Dependency mismatch (`protobuf`) after installing NLP packages.
  - Solution: Pin `protobuf>=3.20,<6` in requirements.
- Long transcript truncation in summarization.
  - Solution: Add chunk-based summarization and final consolidation pass.
- Runtime fragility from model loading and missing packages.
  - Solution: Lazy loading, stronger error handling, and full dependency alignment.
- Upload/record/reload had duplicated processing behavior.
  - Solution: Centralized processing function in UI layer.

## 8) Outcomes

- App now boots cleanly and imports pass consistently.
- Processing path is more stable under common failures.
- Summary quality is more robust for long meetings.
- Added automated checks and documentation for demo readiness.

## 9) Notes

- First run can be slower because Whisper and summarization models may download/cache.
- For production use, replace local JSON auth with a secure database + session management.
