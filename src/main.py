from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from getcontent import generate_page, generate_pages_recursive
import sys

def main():

    basepath = "/"
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]

    #node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(node)

    print(f"Base Path is :{basepath}")
    copy_files_recursive('/home/threep/bootdev/bootStaticSite/static','/home/threep/bootdev/bootStaticSite/docs')
    #generate_page("/home/threep/bootdev/bootStaticSite/content/index.md","/home/threep/bootdev/bootStaticSite/template.html","/home/threep/bootdev/bootStaticSite/public/index.html")
    generate_pages_recursive("/home/threep/bootdev/bootStaticSite/content","/home/threep/bootdev/bootStaticSite/template.html","/home/threep/bootdev/bootStaticSite/docs",basepath)

main()
