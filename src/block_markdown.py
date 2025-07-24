from enum import Enum
import re

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(markdown):

    if re.match('^#{1,6}\s',markdown):
        return BlockType.heading
    elif markdown.startswith('```') and markdown.endswith('```'):
        return BlockType.code
    
    
    lines = markdown.splitlines()

    #Check if quotes
    isQuote = True
    for line in lines:
        #print(f'working on line {line}')
        if not line.startswith('>'):
            isQuote = False
            break
    
    if isQuote:
        return BlockType.quote

    #Check if unordered list
    isUl = True
    for line in lines:
        if not line.startswith('- '):
            isUl = False
            break
    
    if isUl:
        return BlockType.unordered_list


    #Check if ordered list

    isOl = True
    count = 1
    for line in lines:
        if not line.startswith(f'{count}. '):
            isOl = False
            break
        count +=1
    
    if isOl:
        return BlockType.ordered_list
    
    return BlockType.paragraph

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = map(lambda x: x.strip(), blocks)
    cleaned_blocks = []
    for block in blocks:
        if not block == '':
            cleaned_blocks.append(block)
    return cleaned_blocks



def main():
    md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
    print(markdown_to_blocks(md))

if __name__ == "__main__":
    main()