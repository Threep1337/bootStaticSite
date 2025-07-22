import unittest

from htmlnode import HTMLNode, extract_markdown_images,extract_markdown_links
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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/zjjcJKZ2.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image2", "https://i.imgur.com/zjjcJKZ2.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to boot dev2](https://www.boot2.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),("to boot dev2", "https://www.boot2.dev")], matches)

if __name__ == "__main__":
    unittest.main()