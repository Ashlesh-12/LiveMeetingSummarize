import os
import tempfile
import unittest

from export.pdf_export import save_meeting_pdf


SAMPLE_TRANSCRIPT = (
    "Good morning everyone. The team discussed the Q3 roadmap today. "
    "Alice will prepare the design documents by Friday. "
    "Budget review shows we are on track. Bob will send the report."
)
SAMPLE_SUMMARY = (
    "**Meeting Overview**\n"
    "The team reviewed Q3 plans and project status.\n\n"
    "**Key Discussion Points**\n"
    "- Budget is on track\n"
    "- Design documents needed\n\n"
    "**Action Items & Decisions**\n"
    "- Alice will prepare the design documents by Friday\n"
    "- Bob will send the financial report"
)


class TestPdfExport(unittest.TestCase):

    def test_save_meeting_pdf_creates_file(self):
        """filepath mode: should write PDF to disk and return True."""
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "meeting_summary.pdf")
            ok = save_meeting_pdf(
                transcript=SAMPLE_TRANSCRIPT,
                summary=SAMPLE_SUMMARY,
                filepath=out,
                title="Test Meeting",
            )
            self.assertTrue(ok)
            self.assertTrue(os.path.exists(out))
            self.assertGreater(os.path.getsize(out), 1000)

    def test_save_meeting_pdf_returns_bytes_when_filepath_none(self):
        """in-memory mode: should return non-empty bytes when filepath=None."""
        pdf_bytes = save_meeting_pdf(
            transcript=SAMPLE_TRANSCRIPT,
            summary=SAMPLE_SUMMARY,
            filepath=None,
            title="Test Meeting In-Memory",
            action_items=["Follow up with team", "Review budget"],
            username="demo",
            audio_filename="test.wav",
        )
        self.assertIsInstance(pdf_bytes, bytes)
        self.assertGreater(len(pdf_bytes), 1000)
        # PDF magic bytes
        self.assertTrue(pdf_bytes.startswith(b"%PDF"))

    def test_pdf_handles_structured_markdown_summary(self):
        """Structured markdown summary should not raise encoding errors."""
        pdf_bytes = save_meeting_pdf(
            transcript=SAMPLE_TRANSCRIPT,
            summary=SAMPLE_SUMMARY,
            filepath=None,
            title="Meeting Intelligence Report",
        )
        self.assertIsNotNone(pdf_bytes)
        self.assertGreater(len(pdf_bytes), 500)


if __name__ == "__main__":
    unittest.main()
