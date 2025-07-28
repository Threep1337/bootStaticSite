from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from getcontent import generate_page, generate_pages_recursive


def main():
    #node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(node)

    copy_files_recursive('/home/threep/bootdev/bootStaticSite/static','/home/threep/bootdev/bootStaticSite/public')
    #generate_page("/home/threep/bootdev/bootStaticSite/content/index.md","/home/threep/bootdev/bootStaticSite/template.html","/home/threep/bootdev/bootStaticSite/public/index.html")
    generate_pages_recursive("/home/threep/bootdev/bootStaticSite/content","/home/threep/bootdev/bootStaticSite/template.html","/home/threep/bootdev/bootStaticSite/public")

main()
