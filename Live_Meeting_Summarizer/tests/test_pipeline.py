import unittest
from unittest.mock import patch

from pipeline.meeting_pipeline import _chunk_text, _fallback_summary, process_meeting, generate_summary


class TestMeetingPipelineHelpers(unittest.TestCase):
    def test_chunk_text_splits_large_input(self):
        text = " ".join(["word"] * 1301)
        chunks = _chunk_text(text, chunk_size=650)
        self.assertEqual(len(chunks), 3)
        self.assertEqual(len(chunks[0].split()), 650)
        self.assertEqual(len(chunks[1].split()), 650)
        self.assertEqual(len(chunks[2].split()), 1)

    def test_fallback_summary_returns_first_sentences(self):
        """Fallback returns first sentences from realistic text."""
        text = (
            "The team discussed the project timeline today. "
            "Everyone agreed on the new delivery date. "
            "The budget was reviewed and approved by the manager. "
            "Action items were assigned to each department head."
        )
        summary = _fallback_summary(text)
        # Fallback returns up to 4 sentences
        self.assertIn("team discussed", summary)

    def test_generate_summary_is_structured(self):
        """generate_summary produces structured markdown sections for long text."""
        text = (
            "The team discussed the project timeline during the meeting. "
            "Alice will prepare the design documents by Friday. "
            "The budget was reviewed and approved by the finance department. "
            "Bob should share the updated roadmap with all stakeholders. "
            "There are concerns about the deployment schedule needing revision. "
            "Everyone agreed to follow up next Tuesday for the status check. "
        ) * 3  # repeat to get > 50 words
        summary = generate_summary(text)
        self.assertIn("Meeting Overview", summary)

    def test_process_meeting_handles_empty_transcript(self):
        with patch("pipeline.meeting_pipeline.get_full_transcript", return_value=""):
            transcript, summary = process_meeting("dummy.wav")
        self.assertEqual(transcript, "")
        self.assertEqual(summary, "Error: No speech detected or empty transcript")


if __name__ == "__main__":
    unittest.main()
