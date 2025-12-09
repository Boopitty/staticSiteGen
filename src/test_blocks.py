import blocks
import unittest

class TestBlocks(unittest.TestCase):

    # Test the markdown_to_blocks function
    # markdown_to_blocks splits markdown text into blocks separated by double newlines

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

    # Test the block_to_type function
    # block_to_type determines the block type based on markdown syntax

    def test_block_to_type_paragraph(self):
        block = "This is a simple paragraph."
        block_type = blocks.block_to_type(block)
        self.assertEqual(block_type, blocks.BlockType.PARAGRAPH)
    
    def test_block_to_type_heading(self):
        block = "# This is a heading"
        block_type = blocks.block_to_type(block)
        self.assertEqual(block_type, blocks.BlockType.HEADING)
    
    def test_block_to_type_code(self):
        block = "```\nprint('Hello, World!')\n```"
        block_type = blocks.block_to_type(block)
        self.assertEqual(block_type, blocks.BlockType.CODE)

    def test_block_to_type_quote(self):
        block = "> This is a blockquote.\n> It has multiple lines."
        block_type = blocks.block_to_type(block)
        self.assertEqual(block_type, blocks.BlockType.QUOTE)
    
    def test_block_to_type_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        block_type = blocks.block_to_type(block)
        self.assertEqual(block_type, blocks.BlockType.U_LIST)
    
    def test_block_to_type_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        block_type = blocks.block_to_type(block)
        self.assertEqual(block_type, blocks.BlockType.O_LIST)