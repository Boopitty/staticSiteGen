from blocks import markdown_to_blocks, block_to_type, BlockType
from textnode import TextNode, TextType
from htmlnode import ParentNode
from inline import text_to_textnodes

# Convert markdown text to an HTMLNode
def markdown_to_html_node(markdown):
    # Split markdown text into blocks
    blocks = markdown_to_blocks(markdown)
    htmls = []

    # Iterate through each block and convert to corresponding HTMLNode
    for block in blocks:
        blockType = block_to_type(block)
        match blockType:
            case BlockType.PARAGRAPH:
                # handle newlines within paragraph by splitting and joining with spaces
                items = block.split("\n")
                list_items = [item.strip() for item in items if item.strip() != ""]
                htmls.append(ParentNode(tag="p", children=text_to_children(" ".join(list_items))))

            case BlockType.HEADING:
                htmls.append(ParentNode(tag=f"heading", children=text_to_children(block.lstrip("# "))))

            case BlockType.CODE:
                # do not process inline text for code blocks              
                textNode = TextNode(text="<code>" + block.strip("`").lstrip("\n") + "</code>", text_type = TextType.CODE)
                textNode = TextNode.text_node_to_html_node(textNode)
                textNode.tag = "pre"
                htmls.append(textNode)

            case BlockType.QUOTE:
                htmls.append(ParentNode(tag="quote", children=text_to_children(block.lstrip("> "))))

            case BlockType.U_LIST:
                # split by "\n" and create a list of strings
                items = block.split("\n")
                # filter out empty items, strip the leadig "- ", and apply tag
                list_items = ["<li>" + item.lstrip("- ") + "</li>" for item in items if item.strip() != ""]
                htmls.append(ParentNode(tag="ul", children=[text_to_children(item) for item in list_items]))

            case BlockType.O_LIST:
                # split by "\n" and create a list of strings
                items = block.split("\n")
                # filter out empty items, strip the leading numbers, and apply tag
                list_items = ["<li>" + item.lstrip("0123456789. ") + "</li>" for item in items if item.strip() != ""]
                htmls.append(ParentNode(tag="ol", children=[text_to_children(item) for item in list_items]))
    
    return ParentNode(tag="div", children=htmls)

# Convert text to list of HTMLNode children         
def text_to_children(text):
    # Take a string and turn it into a list of TextNodes with appropriate types
    # ex. bold, italic, links, images, code
    text_nodes = text_to_textnodes(text) 
    # convert TextNodes to HTMLNodes
    html_children = [TextNode.text_node_to_html_node(node) for node in text_nodes]
    return html_children
