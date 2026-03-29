import unittest
from inline_md import split_nodes_delimiter
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

if __name__ == "__main__":
    unittest.main()