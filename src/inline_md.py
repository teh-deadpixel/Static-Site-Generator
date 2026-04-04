from textnode import TextType, TextNode
import re 
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:  
            split_by_delimiter = node.text.split(delimiter)
            if len(split_by_delimiter) % 2 == 0:
                raise Exception("Yamete")
            for i in range(len(split_by_delimiter)):
                if not split_by_delimiter[i]:
                    continue
                if i % 2 == 0:
                    result.append(TextNode(split_by_delimiter[i], TextType.TEXT))
                else:
                    result.append(TextNode(split_by_delimiter[i], text_type))
    return result

def extract_markdown_images(text):
    i_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return i_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        elif node.text_type == TextType.TEXT:
            image_matches = extract_markdown_images(node.text)
            if len(image_matches) == 0:
                new_nodes.append(node)
                continue
            remaining_text = node.text
            for tup in image_matches:
                img_alt = tup[0]
                img_link = tup [1]
                split_node = remaining_text.split(f"![{img_alt}]({img_link})", 1)
                remaining_text = split_node[1]
                if split_node[0] != "":
                    new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_link))
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        elif node.text_type == TextType.TEXT:
            link_matches = extract_markdown_links(node.text)
            if len(link_matches) == 0:
                new_nodes.append(node)
                continue
            remaining_text = node.text
            for tup in link_matches:
                link_desc = tup[0]
                link_link = tup [1]
                split_node = remaining_text.split(f"[{link_desc}]({link_link})", 1)
                remaining_text = split_node[1]
                if split_node[0] != "":
                    new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(link_desc, TextType.LINK, link_link))
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes



