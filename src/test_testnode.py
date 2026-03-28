import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()