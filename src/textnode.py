from enum import Enum
from htmlnode import LEAFNODE

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LEAFNODE(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LEAFNODE("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LEAFNODE("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LEAFNODE("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LEAFNODE("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LEAFNODE("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("Text type doko")