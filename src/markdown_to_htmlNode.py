from htmlnode import *
from block_markdown import *

from textnode import TextNode,TextType

def text_to_children(text):
    htmlNodes =[]
    textnodes = text_to_textnodes(text)
    for node in textnodes:
        htmlNodes.append(text_node_to_html_node(node))
    return htmlNodes

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    containerNode = ParentNode("div",children=[])
    for block in markdown_blocks:
        blockType = block_to_block_type(block)
        match blockType:
            case BlockType.paragraph:
                node = ParentNode(tag = "p",children=None)
            case BlockType.heading:
                node = ParentNode(tag = "h",children=None)
            case BlockType.code:
                node = ParentNode(tag = "pre",children=[LeafNode(tag = "code",value=block.lstrip('```\n').rstrip('```'))])
            case BlockType.quote:
                node = ParentNode(tag = "blockquote",children=None)
            case BlockType.unordered_list:
                node = ParentNode(tag = "ul",children=None)
            case BlockType.ordered_list:
                node = ParentNode(tag = "ol",children=None)
        if blockType != BlockType.code:
            node.children = (text_to_children(block))
        containerNode.children.append(node)
    return containerNode
    
def main():
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)

if __name__ == '__main__':
    main()