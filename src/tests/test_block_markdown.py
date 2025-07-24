import unittest
import sys
import os
# Add the parent directory to the path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from block_markdown import markdown_to_blocks,BlockType,block_to_block_type

class TestBlockMarkdown(unittest.TestCase):
        
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_blanklines(self):
        md = """
This is **bolded** paragraph


   


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        blocktype = block_to_block_type("# This is a heading")
        self.assertEqual(blocktype,BlockType.heading)

    def test_block_to_block_type_quote(self):
        md = """> This is a quote
> It is on two lines"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype,BlockType.quote)

    def test_block_to_block_type_Ul(self):
        md = """- This is an unordered list
- It is on two lines"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype,BlockType.unordered_list)

    def test_block_to_block_type_ol(self):
        md = """1. This is an ordered list
2. It is on two lines"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype,BlockType.ordered_list)

    def test_block_to_block_type_paragraph(self):
        md = """1. This is an ordered list
3. But this isnt valid so it should be a paragraph now"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype,BlockType.paragraph)

if __name__ == "__main__":
    unittest.main()