import unittest
from htmlnode import HTMLNODE

class TesthtmlNode(unittest.TestCase):

    def test_multiplePairs(self):
        node = HTMLNODE(None, None, None, {"href": "https://www.google.com", "target": "_blank", "alt": "lore"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" alt="lore"')
    def test_singlePairs(self):
        node1 = HTMLNODE(None, None, None, {"href": "https://www.google.com"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com"')
    def test_NoPairs(self):
        node2 = HTMLNODE(None, None, None, None)
        self.assertEqual(node2.props_to_html(), "")
    
if __name__ == "__main__":
    unittest.main()