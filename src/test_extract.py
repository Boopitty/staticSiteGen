from extract import extract_markdown_images, extract_markdown_links
import unittest

class TestExtract(unittest.TestCase):
    def test_extract_single_image(self):
        text = "Here is an image: ![Alt text](https://example.com/image.png)"
        urls = extract_markdown_images(text)
        self.assertEqual(urls, [("Alt text", "https://example.com/image.png")])
    
    def test_extract_multiple_images(self):
        text = "Images: ![Img1](https://example.com/img1.jpg) and ![Img2](https://example.com/img2.jpg)"
        urls = extract_markdown_images(text)
        self.assertEqual(urls, [("Img1", "https://example.com/img1.jpg"),
                                 ("Img2", "https://example.com/img2.jpg")])
    
    def test_no_images(self):
        text = "This text has no images."
        urls = extract_markdown_images(text)
        self.assertEqual(urls, [])
    
    def test_malformed_image_syntax(self):
        text = "Malformed ![Image](not a url"
        urls = extract_markdown_images(text)
        self.assertEqual(urls, [])
    
    def test_extract_single_link(self):
        text = "Here is a link: [Example](https://example.com)"
        urls = extract_markdown_links(text)
        self.assertEqual(urls, [("Example", "https://example.com")])
    
    def test_extract_multiple_links(self):
        text = "Links: [Google](https://google.com) and [Bing](https://bing.com)"
        urls = extract_markdown_links(text)
        self.assertEqual(urls, [("Google", "https://google.com"),
                                 ("Bing", "https://bing.com")])
    
    def test_no_links(self):
        text = "This text has no links."
        urls = extract_markdown_links(text)
        self.assertEqual(urls, [])
    
    def test_malformed_link_syntax(self):
        text = "Malformed [Link](not a url"
        urls = extract_markdown_links(text)
        self.assertEqual(urls, [])