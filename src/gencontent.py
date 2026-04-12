from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    lines  = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            stripped = line[2:].strip()
            return stripped
    raise Exception("No headers")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    with open(from_path, "r") as f:
        source_md = f.read()
    with open(template_path, "r") as g:
        source_template = g.read()
    
    node = markdown_to_html_node(source_md)
    html_string = node.to_html()
    title = extract_title(source_md)
    template_title = source_template.replace("{{ Title }}", title)
    template_content = template_title.replace("{{ Content }}", html_string)
    href_replace = template_content.replace('href="/', f'href="{basepath}')
    src_replace = href_replace.replace('src="/', f'src="{basepath}')  
    dir = os.path.dirname(dest_path)
    if dir:
        os.makedirs(dir, exist_ok = True)
    with open(dest_path, "w") as h:
        content = h.write(src_replace)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, entry)
        destination_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(source_path):
            generate_page(source_path, template_path, Path(destination_path).with_suffix(".html"), basepath)
            print("Generating pages")
        else:
            generate_pages_recursive(source_path, template_path, destination_path, basepath)