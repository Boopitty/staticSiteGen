import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test equality for identical TextNodes
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        # Test inequality for different TextNodes
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_type(self):
        # Test inequality for different text types
        node = TextNode("Text", TextType.TEXT)
        node2 = TextNode("Text", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        # Test inequality for different URLs
        node = TextNode("Link", TextType.LINK)
        node2 = TextNode("Link", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)
    
    def test_text_plain(self):
        # Test text_to_html_node for plain text
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.children, None)
    
    def test_text_bold(self):
        # Test text_to_html_node for bold text
        node = TextNode("Bold Text", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold Text")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.children, None)
    
    def test_text_italic(self):
        # Test text_to_html_node for italic text
        node = TextNode("Italic Text", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic Text")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.children, None)
    
    def test_text_link(self):
        # Test text_to_html_node for link text
        node = TextNode("Click Here", TextType.LINK, "https://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click Here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})
        self.assertEqual(html_node.children, None)
    
    def test_text_image(self):
        # Test text_to_html_node for image text
        node = TextNode("An image", TextType.IMAGE, "https://example.com/image.png")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "An image"})
        self.assertEqual(html_node.children, None)
        
if __name__ == "__main__":
    unittest.main()