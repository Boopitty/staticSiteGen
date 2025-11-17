import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        # Test props_to_html when there are no properties
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_props(self):
        # Test props_to_html with multiple properties
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_repr(self):
        # Test the __repr__ method of HTMLNode
        node = HTMLNode(tag="p", value="Hello, World!", children=[], props={"class": "intro"})
        expected = "HTMLNode(tag=p, value=Hello, World!, children=[], props={'class': 'intro'})"
        self.assertEqual(repr(node), expected)
    
    def test_leaf_to_html(self):
        node = LeafNode(tag="p", value="Hello,world!")
        self.assertEqual(node.to_html(), "<p>Hello,world!</p>")
    
    def test_leaf_to_html_no_value(self):
        node  = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(tag=None, value="Just some text")
        self.assertEqual(node.to_html(), "Just some text")