from enum import Enum
from htmlnode import PARENTNODE, LEAFNODE
from inline_md import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
def markdown_to_blocks(markdown):
    splitted = markdown.split("\n\n")
    stripped = []
    for st in splitted:
        strip = st.strip()
        if strip == "":
            continue
        stripped.append(strip)
    return stripped

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list" 
    ORDERED_LIST = "ordered_list"

def block_to_block_type(md):
    if md.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if md.startswith("```\n") and md.endswith("```"):
        return BlockType.CODE
    if md.startswith(">"):
        lines = md.split("\n")
        for line in lines:
            if  not line.startswith(">"):
                return BlockType.PARAGRAPH
            else:
                continue
        return BlockType.QUOTE
    if md.startswith("- "):
        lines = md.split("\n")
        for line in lines:
            if  not line.startswith("- "):
                return BlockType.PARAGRAPH
            else:
                continue
        return BlockType.UNORDERED_LIST
    
    if md.startswith("1. "):
        i = 1
        lines = md.split("\n")
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes
    
def paragraph_to_html_node(block):
    lines = block.split("\n")
    joined_lines = " ".join(lines)
    html_nodes = text_to_children(joined_lines)
    parent = PARENTNODE("p", html_nodes)
    return parent

def heading_to_html_node(block):
    hashes = 0
    for ch in block:
        if ch == "#":
            hashes += 1
        else:
            break
    stripped = block[hashes+1:]
    html_nodes = text_to_children(stripped)
    parent = PARENTNODE(f"h{hashes}", html_nodes)
    return parent

def code_to_html_node(block):
    stripped = block[4:-3]
    text_node = TextNode(stripped, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    child  = PARENTNODE("code", [html_node])
    parent = PARENTNODE("pre", [child])
    return parent

def quote_to_html_node(block):
    lines = block.split("\n")
    stripped = []
    for line in lines:
        space_strip = line[1:].strip()
        stripped.append(space_strip)
    joined_lines = " ".join(stripped)
    html_node = text_to_children(joined_lines)
    parent = PARENTNODE("blockquote", html_node)
    return parent
"""
for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        stripped.append(line.strip(">").strip())

        inner_content = "\n".join(stripped)
        paragraphs = inner_content.split("\n\n")

        children = []
        for para in paragraphs:
            text = para.replace("\n", " ").strip()
            if text:
                p_children = text_to_children(text)
                children.append(PARENTNODE("p", p_children))
    parent = PARENTNODE("blockquote", children)
    return parent
"""

def ulist_to_html_node(block):
    lines = block.split("\n")
    child = []
    for line in lines:
        stripped = line[2:]
        c_nodes = text_to_children(stripped)
        child.append(PARENTNODE("li", c_nodes))
    parent = PARENTNODE("ul", child)
    return parent

def olist_to_html_node(block):
    lines = block.split("\n")
    child = []
    for line in lines:
        dot_split = line.split(". ")
        stripped = dot_split[1]
        html_node = text_to_children(stripped)
        child.append(PARENTNODE("li", html_node))
    parent = PARENTNODE("ol", child)
    return parent

def block_to_html_node(block):
    
    
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return PARENTNODE("div", children)