

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