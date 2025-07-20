import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq_DiffText(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a differenttext node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_neq_DiffTextType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a differenttext node", TextType.CODE)
        self.assertNotEqual(node,node2)
    
    def test_eq_withUrl(self):
        node = TextNode("This is a text node", TextType.BOLD,url="www.google.ca")
        node2 = TextNode("This is a text node", TextType.BOLD,url="www.google.ca")
        self.assertEqual(node, node2)

    def test_neq_withUrlInOne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,url="www.google.ca")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()