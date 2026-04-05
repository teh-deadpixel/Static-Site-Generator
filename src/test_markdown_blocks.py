import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
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
            
        def test_markdown_to_blocks_split(self):
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

        def test_markdown_to_blocks_blank_lines(self):
            md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertNotIn("", blocks)
               
class TestBlockToBlocKTypes(unittest.TestCase):
    def test_heading(self):
        md = "###### Bleh"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.HEADING )
    def test_heading_min_limit(self):
        md = "####### bleh"
        block = block_to_block_type(md)
        self.assertEqual(block, BlockType.PARAGRAPH)
    def test_code(self):
         md = "```\nsnek\n```"
         block = block_to_block_type(md)
         self.assertEqual(block, BlockType.CODE)
    def test_code_no_end_ticks(self):
         md = "```\nsnek\n"
         block = block_to_block_type(md)
         self.assertEqual(block, BlockType.PARAGRAPH)

#more testcases to be added
    
            
if __name__ == "__main__":
    unittest.main()