from enum import Enum
from htmlnode import LeafNode, ParentNode

class TextType(Enum):
    # All possible text types
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    # Unused types for potential future use
    # DIV = "div"
    # SPAN = "span"

class TextNode():
    def __init__(self, text="", text_type="text", url=None):
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
    
    def text_node_to_html_node(text_node):
        # make an HTMLNode from a TextNode
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(tag=None, value=text_node.text)
            case TextType.BOLD:
                return LeafNode(tag="b", value=text_node.text)
            case TextType.ITALIC:
                return LeafNode(tag="i", value=text_node.text)
            case TextType.CODE:
                return LeafNode(tag="code", value=text_node.text)
            case TextType.LINK:
                return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
            case TextType.IMAGE:
                return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
              