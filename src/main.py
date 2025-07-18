from textnode import TextNode,TextType


def main():
    node = TextNode("test",TextType.BOLD,"www.test.ca")
    print(f"{node}")


main()