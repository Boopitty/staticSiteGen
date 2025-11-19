class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        # String of HTML tag name (e.g., "a", "div", "p")
        self.tag = tag
        # String of the value of the HTML tag (e.g., text in a paragraph)
        self.value = value
        # List of child HTMLNode objects
        self.children = children
        # Dictionary of attributes of the HTML tag (e.g., {"href": "https://example.com"})
        self.props = props

    def to_html(self):
        # Convert the HTMLNode and its children to an HTML string
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        # Convert props dictionary to HTML attributes string
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self):
        # String representation of the HTMLNode
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # LeafNode MUST have a tag and a value.
        # LeafNode NEVER has children. props is optional.
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        # Convert the LeafNode to an HTML string
        if self.value is None:
            # if no value, cannot convert to HTML
            raise ValueError("LeafNode must have a value to convert to HTML")
        if self.tag is None:
            # if no tag, print raw value
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children=[], props=None):
        # ParentNode MUST have a tag and children.
        # ParentNode NEVER has a value. props is optional.
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        # Check for tag and children
        if not self.tag:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if not self.children:
            raise ValueError("ParentNode must have children to convert to HTML")
        # Return HTML string with children converted to HTML
        return f"<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"