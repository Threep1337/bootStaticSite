from markdown_blocks import markdown_to_html_node
from extracttitle import extract_title
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



def main():
    pass

if __name__ == "__main__":
    main()