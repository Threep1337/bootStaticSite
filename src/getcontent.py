import re
from markdown_blocks import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        # f is a file object
        from_path_contents = f.read()

    with open(template_path) as f:
        # f is a file object
        template_path_contents = f.read()
    
    html = markdown_to_html_node(from_path_contents).to_html()
    title = extract_title(from_path_contents)
    template_path_contents = template_path_contents.replace("{{ Title }}",title)
    template_path_contents = template_path_contents.replace("{{ Content }}",html)
    
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as f:
        f.write(template_path_contents)


def extract_title(markdown):
    match = re.match("# (.+)",markdown)
    if match:
        return (match.group(1).strip())
    else:
        raise Exception("No valid title found in markdown.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        fullpath = os.path.join(dir_path_content,file)
        if os.path.isfile(fullpath):
            destpath = os.path.join(dest_dir_path,file)
            destpath = os.path.splitext(destpath)[0]
            destpath += '.html'
            print(f"dest path is {destpath}")
            generate_page(fullpath, template_path,destpath)
        else:
            generate_pages_recursive(fullpath, template_path, os.path.join(dest_dir_path,file))

def main():
    print(extract_title("# Hello"))

if __name__ == '__main__':
    main()