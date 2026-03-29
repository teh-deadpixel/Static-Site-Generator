import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_image(self):
        node3 = TextNode("alt text description", TextType.IMAGE, "https://example.com/photo.png")
        node4 = TextNode("alt text description(bear)", TextType.IMAGE, "https://example2.com/photo.png")
        self.assertNotEqual(node3, node4)
    def test_link(self):
        node5 = TextNode("alt text description", TextType.LINK)
        node6 = TextNode("alt text description", TextType.LINK, "https://www.example.com")
        self.assertNotEqual(node5, node6)

class TestTextType(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_Bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("alt text description", TextType.LINK, "https://www.example.com")
        hmtl_node = text_node_to_html_node(node)
        self.assertEqual(hmtl_node.tag, "a")
        self.assertEqual(hmtl_node.value, "alt text description" )
        self.assertEqual(hmtl_node.props, {"href": "https://www.example.com"})
    def test_image(self):
         node = TextNode("alt text description", TextType.IMAGE, "https://example.com/photo.png")
         hmtl_node = text_node_to_html_node(node)
         self.assertEqual(hmtl_node.tag, "img")
         self.assertEqual(hmtl_node.value, "" )
         self.assertEqual(hmtl_node.props, {"src": "https://example.com/photo.png", "alt": "alt text description"})


if __name__ == "__main__":
    unittest.main()