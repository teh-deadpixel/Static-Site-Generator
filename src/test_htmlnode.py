import unittest
from htmlnode import HTMLNODE, LEAFNODE, PARENTNODE


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
class TestLeafNode(unittest.TestCase):
    def test_NormalTag(self):
        l_node = LEAFNODE("p",  "This is a paragraph of text.", None)
        self.assertEqual(l_node.to_html(), "<p>This is a paragraph of text.</p>")
    def test_PropTag(self):
        l_node1 = LEAFNODE("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(l_node1.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_tag(self):
        l_node2 = LEAFNODE(None, "Ano Eto Bweh")
        self.assertEqual(l_node2.to_html(), "Ano Eto Bweh")
    def test_MissingValue(self):
        l_node3 = LEAFNODE("p", None)
        self.assertRaises(ValueError, l_node3.to_html)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LEAFNODE("span", "child")
        parent_node = PARENTNODE("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LEAFNODE("b", "grandchild")
        child_node = PARENTNODE("span", [grandchild_node])
        parent_node = PARENTNODE("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_no_tag(self):
        child_node = LEAFNODE("p","child")
        parent_node = PARENTNODE(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
    
    def test_to_html_with_no_children(self):
        child_node = LEAFNODE("span", "child")
        parent_node = PARENTNODE("div",None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_multiple_child_types(self):
        grandchild_node = LEAFNODE(None, "grandchild")
        child_node = LEAFNODE("span", "child")
        parent_node = PARENTNODE("div", [child_node, grandchild_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span>grandchild</div>")
    def test_to_html_with_parent_props(self):
        child_node = LEAFNODE("p","child")
        parent_node = PARENTNODE("a", [child_node], {"href": "https://www.google.com"})
        self.assertEqual(parent_node.to_html(), '<a href="https://www.google.com"><p>child</p></a>')

if __name__ == "__main__":
    unittest.main()
