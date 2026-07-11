import unittest
from unittest.mock import patch

from pipeline.meeting_pipeline import _chunk_text, _fallback_summary, process_meeting


class TestMeetingPipelineHelpers(unittest.TestCase):
    def test_chunk_text_splits_large_input(self):
        text = " ".join(["word"] * 1301)
        chunks = _chunk_text(text, chunk_size=650)
        self.assertEqual(len(chunks), 3)
        self.assertEqual(len(chunks[0].split()), 650)
        self.assertEqual(len(chunks[1].split()), 650)
        self.assertEqual(len(chunks[2].split()), 1)

    def test_fallback_summary_returns_first_sentences(self):
        text = "One. Two. Three. Four. Five. Six."
        summary = _fallback_summary(text)
        self.assertEqual(summary, "One. Two. Three. Four.")

    def test_process_meeting_handles_empty_transcript(self):
        with patch("pipeline.meeting_pipeline.get_full_transcript", return_value=""):
            transcript, summary = process_meeting("dummy.wav")
        self.assertEqual(transcript, "")
        self.assertEqual(summary, "Error: No speech detected or empty transcript")


if __name__ == "__main__":
    unittest.main()
