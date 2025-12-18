import main
import unittest

class TestMain(unittest.TestCase):

    def test_extract_title_with_h1(self):
        markdown = "# This is a Title\nSome content here."
        title = main.extract_title(markdown)
        self.assertEqual(title, "# This is a Title")

    def test_extract_title_without_h1(self):
        markdown = "## This is a Subtitle\nSome content here."
        with self.assertRaises(Exception) as context:
            main.extract_title(markdown)
        self.assertTrue("No h1 header found in markdown" in str(context.exception))

    def test_extract_title_with_leading_blank_lines(self):
        markdown = "\n\n# Leading Title\nContent follows."
        title = main.extract_title(markdown)
        self.assertEqual(title, "# Leading Title")

    def test_extract_title_with_no_content(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            main.extract_title(markdown)
        self.assertTrue("No h1 header found in markdown" in str(context.exception))
