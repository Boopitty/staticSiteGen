from enum import Enum

class TextType(Enum):
    # All possible text types
    plain = "plain"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

class TextNode():
    def __init__(self, text="", text_type="plain", url=None):
        # String of text content
        self.text = text
        # Type of text (from TextType enum)
        self.text_type = text_type
        # URL for links or images (if applicable)
        self.url = url
    
    def __eq__(self, other):
        # Equality check based on text, type, and URL
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        # String representation of the TextNode
        return f"TextNode({self.text}, {self.text_type}, {self.url})"