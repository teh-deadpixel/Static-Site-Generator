import unittest
from inline_md import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_codeblock(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split_node, [TextNode("This is text with a ", TextType.TEXT), 
                                      TextNode("code block", TextType.CODE), 
                                      TextNode(" word", TextType.TEXT),])

    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("This is text with a ", TextType.TEXT),
                                      TextNode("bolded phrase", TextType.BOLD),
                                      TextNode(" in the middle", TextType.TEXT),])
    
    def test_not_text(self):
        node = TextNode("bolded phrase", TextType.BOLD)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [TextNode("bolded phrase", TextType.BOLD)])

    def test_unclosed_delimiter(self):
        node = TextNode("This is text with a **bolded phrase in the middle", TextType.TEXT)
        self.assertRaises(Exception,split_nodes_delimiter,[node], "**", TextType.BOLD)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_multiple_images(self):
         matches = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
         self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    def test_incorrect_input_image(self):
        matches = extract_markdown_images("This is text with an [image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),], matches)
    
    def test_incorrect_input_link(self):
        matches = extract_markdown_links("This is text with a link ![to boot dev](https://www.boot.dev)")
        self.assertListEqual([], matches)
    
    def test_multiple_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

if __name__ == "__main__":
    unittest.main()