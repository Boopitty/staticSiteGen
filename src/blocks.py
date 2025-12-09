from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

# This function converts markdown text into blocks separated by double newlines
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            new_blocks.append(stripped_block)
    return new_blocks

# Determine the block type based on markdown syntax
def block_to_type(block):
    # Heading syntax: 1 to 6 #s followed by a space and text
    if re.match(r"#{1,6} \S+", block):
        return BlockType.HEADING
    
    # Code block syntax: triple backticks
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Quote syntax: lines starting with >
    elif block.startswith("> "):
        for line in block.split("\n"):
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    # Unordered list syntax: lines starting with -
    elif block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.U_LIST
    
    # Ordered list syntax: lines starting with 1., 2., etc.
    elif block.startswith("1. "):
        count = 1
        # Check each line for correct numbering
        for line in block.split("\n"):
            if not line.startswith(f"{count}. "):
                return BlockType.PARAGRAPH
            count += 1
        return BlockType.O_LIST
    
    else:
        return BlockType.PARAGRAPH
