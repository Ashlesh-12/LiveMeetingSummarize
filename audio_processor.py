"""
Audio Processing Module - Processes real uploaded audio files
Uses OpenAI Whisper for transcription
"""

import streamlit as st
import whisper
import tempfile
import os
from datetime import datetime, timedelta

class AudioProcessor:
    def __init__(self, model_name="base"):
        """Initialize Whisper model"""
        try:
            self.model = whisper.load_model(model_name)
            self.model_name = model_name
        except Exception as e:
            st.error(f"Failed to load Whisper model: {str(e)}")
            self.model = None
    
    def transcribe_audio(self, audio_file):
        """
        Transcribe audio file using Whisper
        
        Args:
            audio_file: Streamlit uploaded file object
            
        Returns:
            dict: Contains transcript, segments, and metadata
        """
        if self.model is None:
            return {
                "error": "Model not loaded",
                "transcript": "",
                "segments": []
            }
        
        try:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(audio_file.getbuffer())
                tmp_path = tmp_file.name
            
            # Transcribe
            result = self.model.transcribe(tmp_path)
            
            # Extract transcript
            full_transcript = result.get("text", "")
            
            # Extract segments with timestamps
            segments = []
            for segment in result.get("segments", []):
                start_time = self._format_time(segment["start"])
                end_time = self._format_time(segment["end"])
                text = segment.get("text", "").strip()
                
                if text:  # Only add non-empty segments
                    segments.append({
                        "start": start_time,
                        "end": end_time,
                        "text": text,
                        "start_seconds": segment["start"],
                        "end_seconds": segment["end"]
                    })
            
            # Clean up
            os.unlink(tmp_path)
            
            return {
                "error": None,
                "transcript": full_transcript,
                "segments": segments,
                "duration": result.get("duration", 0),
                "language": result.get("language", "en")
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "transcript": "",
                "segments": []
            }
    
    @staticmethod
    def _format_time(seconds):
        """Convert seconds to MM:SS format"""
        mins = int(seconds) // 60
        secs = int(seconds) % 60
        return f"{mins}:{secs:02d}"

class SpeakerDiarizer:
    """
    Assign speakers to transcript segments
    (Simplified version - assigns Speaker 1, 2, etc. based on pauses)
    """
    
    @staticmethod
    def diarize_segments(segments):
        """
        Assign speaker labels to segments
        
        Args:
            segments: List of transcript segments
            
        Returns:
            List of segments with speaker assignments
        """
        if not segments:
            return []
        
        diarized = []
        current_speaker = 1
        last_end_time = 0
        SPEAKER_CHANGE_THRESHOLD = 0.5  # Pause threshold in seconds
        
        for segment in segments:
            # Check if there's a significant pause (indicate speaker change)
            if segment["start_seconds"] - last_end_time > SPEAKER_CHANGE_THRESHOLD:
                current_speaker = 2 if current_speaker == 1 else 1
            
            diarized.append({
                "speaker": f"Speaker {current_speaker}",
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"],
                "start_seconds": segment["start_seconds"],
                "end_seconds": segment["end_seconds"]
            })
            
            last_end_time = segment["end_seconds"]
        
        return diarized

class SummaryGenerator:
    """Generate summaries from transcripts"""
    
    @staticmethod
    def generate_summary(transcript):
        """
        Generate a summary from transcript
        
        Args:
            transcript: Full transcript text
            
        Returns:
            str: Summary text
        """
        if not transcript or len(transcript.strip()) < 50:
            return "Transcript too short to summarize."
        
        try:
            from transformers import pipeline
            
            # Use BART for summarization
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            
            # Split into chunks if too long (max 1024 tokens)
            words = transcript.split()
            chunks = []
            current_chunk = []
            
            for word in words:
                current_chunk.append(word)
                if len(current_chunk) >= 400:  # ~400 words per chunk
                    chunks.append(" ".join(current_chunk))
                    current_chunk = []
            
            if current_chunk:
                chunks.append(" ".join(current_chunk))
            
            # Summarize first chunk
            if chunks:
                summary_result = summarizer(chunks[0], max_length=150, min_length=50, do_sample=False)
                return summary_result[0]["summary_text"]
            
            return "Unable to generate summary."
            
        except Exception as e:
            # Fallback: Return first 2 sentences
            sentences = transcript.split(".")
            return ". ".join(sentences[:2]) + "."
