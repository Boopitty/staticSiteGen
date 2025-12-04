import blocks
import unittest

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        new_blocks = blocks.markdown_to_blocks(md)
        self.assertEqual(new_blocks,
                         [
                             "This is **bolded** paragraph",
                             "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                             "- This is a list\n- with items"
                         ])
        
    def test_markdown_to_blocks_empty_string(self):
        md = ""
        new_blocks = blocks.markdown_to_blocks(md)
        self.assertEqual(new_blocks, [])

    def test_markdown_to_blocks_single_block(self):
        md = "This is a single block"
        new_blocks = blocks.markdown_to_blocks(md)
        self.assertEqual(new_blocks, ["This is a single block"])

    def test_markdown_to_blocks_multiple_empty_lines(self):
        md = "Block 1\n\n\n\nBlock 2"
        new_blocks = blocks.markdown_to_blocks(md)
        self.assertEqual(new_blocks, ["Block 1", "Block 2"])

    def test_markdown_to_blocks_whitespace_only(self):
        md = "   \n\n   \n\n   "
        new_blocks = blocks.markdown_to_blocks(md)
        self.assertEqual(new_blocks, [])

    def test_markdown_to_blocks_leading_trailing_whitespace(self):
        md = "  Block with spaces  \n\n  Another block  "
        new_blocks = blocks.markdown_to_blocks(md)
        self.assertEqual(new_blocks, ["Block with spaces", "Another block"])
