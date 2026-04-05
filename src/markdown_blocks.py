from enum import Enum

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