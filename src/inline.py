import re
from textnode import TextNode, TextType

# Split a list of markdown TextNodes by a delimiter for a given text type
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # If node is not of the specified text_type, keep it as is
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text == "":
            new_nodes.append(node)
            continue
        delimiters = 0

        # Count pairs of delimiters
        for char in node.text:
            if char == delimiter:
                delimiters += 1

        # If delimiter count is even, continue, else raise exception
        if delimiters % 2 == 0:
            segments = node.text.split(delimiter)
            # Reconstruct nodes based on segments
            for i in range(len(segments)):
                if segments[i] != "":
                    if i % 2 == 0:
                        new_nodes.append(TextNode(segments[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(segments[i], text_type))
        else:
            raise ValueError("Unmatched delimiter found in text.")        
         
    return new_nodes
    
def extract_markdown_images(text):
    # Extract markdown image URLs from text
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # Extract markdown link URLs from text
    pattern = r"(?<!\!)\[([^\[\]]+)\]\(([^\(\)]+)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    # take markdown text and split it into textNodes for images and text
    nodes = [] 
    pattern = r"!\[[^\[\]]*\]\([^\(\)]*\)" # patern to match markdown image syntax ![alt text](url)

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # if not plain text, just add node as is
            nodes.append(node)
            continue
        
        # Extract image patterns and split text into segments that don't include the image markdowns
        text = node.text 
        images = extract_markdown_images(text)
        segments = re.split(pattern, text)

        while text:
            # check which segment or image is at the start of the remaining text
            # add corresponding TextNode to nodes list
            # text becomes shorter each iteration until empty

            if segments and text.startswith(segments[0]):
                seg = segments.pop(0)
                if seg != "":
                    nodes.append(TextNode(seg, TextType.TEXT))
                text = text[len(seg):]

            elif images and text.startswith(f"![{images[0][0]}]({images[0][1]})"):
                alt_text, url = images.pop(0)
                nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                text = text[len(f"![{alt_text}]({url})"):]

            else:
                # if neither segment nor image is at start, just add remaining text as TextNode and break
                nodes.append(TextNode(text, TextType.TEXT))
                break
    # if no nodes are added, return the original list
    return nodes if nodes else old_nodes

def split_nodes_link(old_nodes):
    nodes = []
    pattern = r"(?<!\!)\[[^\[\]]+\]\([^\(\)]+\)"

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(text)
        segments = re.split(pattern, text)

        while text:
            if segments and text.startswith(segments[0]):
                seg = segments.pop(0)
                if seg != "":
                    nodes.append(TextNode(seg, TextType.TEXT))
                text = text[len(seg):]

            elif links and text.startswith(f"[{links[0][0]}]({links[0][1]})"):
                link_text, url = links.pop(0)
                nodes.append(TextNode(link_text, TextType.LINK, url))
                text = text[len(f"[{link_text}]({url})"):]

            else:
                nodes.append(TextNode(text, TextType.TEXT))
                break
    return nodes if nodes else old_nodes

def text_to_textnodes(text):
    # Convert a string of text into a list of TextNodes with appropriate types
    nodes = [TextNode(text, TextType.TEXT)]
    
    for delimiter, text_type in [("_", TextType.ITALIC), ("**", TextType.BOLD), ("`", TextType.CODE)]:
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes