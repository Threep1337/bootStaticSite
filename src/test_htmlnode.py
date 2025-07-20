import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_equal(self):
        node = HTMLNode(tag="a",value="this is a test",props = {"href": "https://www.google.com","target": "_blank"})
        node_props_html = node.props_to_html()
        self.assertEqual(node_props_html,' href="https://www.google.com" target="_blank"')
    
    def test_props_to_html_not_equal(self):
        node = HTMLNode(tag="a",value="this is a test",props = {"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode(tag="a",value="this is a test",props = {"href": "https://www.google.com","target": "SomethingElse"})
        node_props_html = node.props_to_html()
        node2_props_html = node2.props_to_html()
        self.assertNotEqual(node_props_html,node2_props_html)
    
    def test_props_to_html_not_equal_moreProps(self):
        node = HTMLNode(tag="a",value="this is a test",props = {"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode(tag="a",value="this is a test",props = {"href": "https://www.google.com","target": "SomethingElse","prop3":"TEST"})
        node_props_html = node.props_to_html()
        node2_props_html = node2.props_to_html()
        self.assertNotEqual(node_props_html,node2_props_html)

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="a",value="this is a test")
        node_props_html = node.props_to_html()
        self.assertEqual(node_props_html,'')

if __name__ == "__main__":
    unittest.main()