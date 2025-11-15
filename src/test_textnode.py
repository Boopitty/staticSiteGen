import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a different text node", TextType.bold)
        self.assertNotEqual(node, node2)
    
    def test_type(self):
        node = TextNode("Text", TextType.plain)
        node2 = TextNode("Text", TextType.italic)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("Link", TextType.link)
        node2 = TextNode("Link", TextType.link, "https://different.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()