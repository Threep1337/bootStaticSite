import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_noTag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_withProps(self):
        node = LeafNode("a", "Hello, world!",props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Hello, world!</a>")

if __name__ == "__main__":
    unittest.main()