import mark_to_html
import unittest

class TestMarkToHTML(unittest.TestCase):
    def test_markdown_to_html_node_paragraph(self):
        markdown = "This is a paragraph."
        html_node = mark_to_html.markdown_to_html_node(markdown)
        expected_html = '<div><p>This is a paragraph.</p></div>'
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_heading(self):
        markdown = "# This is a heading"
        html_node = mark_to_html.markdown_to_html_node(markdown)
        expected_html = '<div><heading>This is a heading</heading></div>'
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_code(self):
        markdown = "```\nprint('Hello, World!')\n```"
        html_node = mark_to_html.markdown_to_html_node(markdown)
        expected_html = '<div><pre><code>print(\'Hello, World!\')\n</code></pre></div>'
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_quote(self):
        markdown = "> This is a quote."
        html_node = mark_to_html.markdown_to_html_node(markdown)
        expected_html = '<div><quote>This is a quote.</quote></div>'
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_unordered_list(self):
        markdown = "- Item 1\n- Item 2\n- Item 3"
        html_node = mark_to_html.markdown_to_html_node(markdown)
        expected_html = '<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>'
        self.assertEqual(html_node.to_html(), expected_html)

    def test_markdown_to_html_node_ordered_list(self):
        markdown = "1. First\n2. Second\n3. Third"
        html_node = mark_to_html.markdown_to_html_node(markdown)
        expected_html = '<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>'
        self.assertEqual(html_node.to_html(), expected_html)
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
        
"""

        node = mark_to_html.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = mark_to_html.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )