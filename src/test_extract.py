from extract import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
import unittest # unittest will run all test_functions

class TestExtract(unittest.TestCase):

    # SPLIT NODES DELIMITER TESTS
    # the split nodes delimiter function takes a list of textNodes and splits them
    # by a given delimiter for a given text type
    # a a new list of textNodes is returned including the new text types

    def test_split_nodes_delimiter(self):
        # Test split_nodes_delimiter method with multiple delimiters
        old_nodes1 = [TextNode("This is *some* text with *delimiters*", TextType.TEXT)]
        new_nodes1 = split_nodes_delimiter(old_nodes1, "*", TextType.BOLD)
        self.assertEqual(new_nodes1, [TextNode("This is ", TextType.TEXT),
                                     TextNode("some", TextType.BOLD),
                                     TextNode(" text with ", TextType.TEXT),
                                     TextNode("delimiters", TextType.BOLD)])
        
    def test_split_nodes_delimiter_edge(self):
        # Test split_nodes_delimiter with delimiter at start
        old_nodes = [TextNode("_delimiter_ at the start", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("delimiter", TextType.ITALIC),
                                     TextNode(" at the start", TextType.TEXT)])
    
    def test_split_nodes_delimiter_no_delimiters(self):
        # Test split_nodes_delimiter with no delimiters
        old_nodes = [TextNode("No delimiters here", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("No delimiters here", TextType.TEXT)])
     
    def test_split_nodes_delimiter_raise(self):
        # Test split_nodes_delimiter raises error for odd delimiters
        old_nodes = [TextNode("This is *an error", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "*", TextType.BOLD)
    
    # EXTRACT MARKDOWN IMAGES TESTS
    # the extract_markdown_images function takes a string of text
    # and returns a list of tuples with the alt text and url of each image found

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
    
    # EXTRACT MARKDOWN LINKS TESTS
    # the extract_markdown_links function takes a string of text
    # and returns a list of tuples with the link text and url of each link found

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
    
    # SPLIT NODES IMAGE TESTS
    # the split_nodes_image function takes a list of textNodes
    # and splits any markdown image syntax into separate textNodes
    # the split_nodes_image function also makes use of the extract_markdown_images function

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_no_images(self):
        node = TextNode("This is just plain text.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is just plain text.", TextType.TEXT)], new_nodes)
    
    def test_split_images_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("", TextType.TEXT)], new_nodes)
    
    def test_split_images_start(self):
        node = TextNode("![start_image](https://example.com) is at the start.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("start_image", TextType.IMAGE, "https://example.com"),
                TextNode(" is at the start.", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_split_images_end(self):
        node = TextNode("This is at the end ![end_image](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is at the end ", TextType.TEXT),
                TextNode("end_image", TextType.IMAGE, "https://example.com"),
            ],
            new_nodes
        )
    
    def test_split_images_consecutive(self):
        node = TextNode("Consecutive ![img1](url1)![img2](url2) images.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Consecutive ", TextType.TEXT),
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode("img2", TextType.IMAGE, "url2"),
                TextNode(" images.", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_split_images_only_image(self):
        node = TextNode("![only_image](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("only_image", TextType.IMAGE, "https://example.com"),
            ],
            new_nodes
        )
    
    def test_split_images_with_link(self):
        node = TextNode(
            "Image ![img](https://example.com/image.png) and link [link](https://example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Image ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(" and link [link](https://example.com)", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_images_list_of_nodes(self):
        # this test iclude a variety of situations including nodes that are not plain text
        nodes = [
            TextNode("First node with ![img1](url1)", TextType.TEXT),
            TextNode("Second node without image", TextType.TEXT),
            TextNode("Third node with ![img2](url2) and ![img3](url3)", TextType.TEXT),
            TextNode("Fourth node is bold", TextType.BOLD),
            TextNode("Fifth node is link", TextType.LINK, "https://example.com"),
            TextNode("Sixth node is image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode("Seventh node with [link](https://example.com)", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("First node with ", TextType.TEXT),
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode("Second node without image", TextType.TEXT),
                TextNode("Third node with ", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "url2"),
                TextNode(" and ", TextType.TEXT),
                TextNode("img3", TextType.IMAGE, "url3"),
                TextNode("Fourth node is bold", TextType.BOLD),
                TextNode("Fifth node is link", TextType.LINK, "https://example.com"),
                TextNode("Sixth node is image", TextType.IMAGE, "https://example.com/image.png"),
                TextNode("Seventh node with [link](https://example.com)", TextType.TEXT),
            ],
            new_nodes,
        )
    
    # SPLIT NODES LINK TESTS
    # the split_nodes_link function takes a list of textNodes
    # and splits any markdown link syntax into separate textNodes
    # the split_nodes_link function also makes use of the extract_markdown_links function

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )
    
    def test_split_links_no_links(self):
        node = TextNode("This is just plain text.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is just plain text.", TextType.TEXT)], new_nodes)
    
    def test_split_links_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("", TextType.TEXT)], new_nodes)
    
    def test_split_links_start(self):
        node = TextNode("[start_link](https://example.com) is at the start.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("start_link", TextType.LINK, "https://example.com"),
                TextNode(" is at the start.", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_split_links_end(self):
        node = TextNode("This is at the end [end_link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is at the end ", TextType.TEXT),
                TextNode("end_link", TextType.LINK, "https://example.com"),
            ],
            new_nodes
        )
    
    def test_split_links_consecutive(self):
        node = TextNode("Consecutive [link1](url1)[link2](url2) links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Consecutive ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode("link2", TextType.LINK, "url2"),
                TextNode(" links.", TextType.TEXT),
            ],
            new_nodes
        )
    
    def test_split_links_only_link(self):
        node = TextNode("[only_link](https://example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("only_link", TextType.LINK, "https://example.com"),
            ],
            new_nodes
        )
    
    def test_split_links_with_image(self):
        node = [
            TextNode(
                "Link [link](https://example.com) and image ![img](https://example.com/image.png)",
                TextType.TEXT,
            )
        ]
        new_nodes = split_nodes_link(node)
        self.assertListEqual(
            [
                TextNode("Link ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and image ![img](https://example.com/image.png)", TextType.TEXT),
            ],
            new_nodes
        )

    def test_split_links_list_of_nodes(self):
        # this test iclude a variety of situations including nodes that are not plain text
        nodes = [
            TextNode("First node with [link1](url1)", TextType.TEXT),
            TextNode("Second node without link", TextType.TEXT),
            TextNode("Third node with [link2](url2) and [link3](url3)", TextType.TEXT),
            TextNode("Fourth node is italic", TextType.ITALIC),
            TextNode("Fifth node is an image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode("Sixth node is link", TextType.LINK, "https://example.com"),
            TextNode("Seventh node with ![image](https://example.com/image.png)", TextType.TEXT),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("First node with ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode("Second node without link", TextType.TEXT),
                TextNode("Third node with ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "url2"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link3", TextType.LINK, "url3"),
                TextNode("Fourth node is italic", TextType.ITALIC),
                TextNode("Fifth node is an image", TextType.IMAGE, "https://example.com/image.png"),
                TextNode("Sixth node is link", TextType.LINK, "https://example.com"),
                TextNode("Seventh node with ![image](https://example.com/image.png)", TextType.TEXT),
            ],
            new_nodes,
        )