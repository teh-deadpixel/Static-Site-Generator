from textnode import TextType, TextNode

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
                