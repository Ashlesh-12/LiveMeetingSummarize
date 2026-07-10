import os
import tempfile
import unittest

from export.pdf_export import save_meeting_pdf


class TestPdfExport(unittest.TestCase):
    def test_save_meeting_pdf_creates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "meeting_summary.pdf")
            ok = save_meeting_pdf(
                transcript="Line one\nLine two",
                summary="Summary line one.\nSummary line two.",
                filepath=out,
                title="Test Meeting",
            )
            self.assertTrue(ok)
            self.assertTrue(os.path.exists(out))
            self.assertGreater(os.path.getsize(out), 0)


if __name__ == "__main__":
    unittest.main()
