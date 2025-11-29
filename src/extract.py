import re

def extract_markdown_images(text):
    # Extract markdown image URLs from text
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # Extract markdown link URLs from text
    pattern = r"\[([^\[\]]+)\]\(([^\(\)]+)\)"
    matches = re.findall(pattern, text)
    return matches
    