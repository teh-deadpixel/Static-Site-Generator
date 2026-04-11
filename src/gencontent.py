from markdown_blocks import markdown_to_html_node
import os

def extract_title(markdown):
    lines  = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            stripped = line[2:].strip()
            return stripped
    raise Exception("No headers")

def generate_page(from_path, template_path, dest_path):
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
    dir = os.path.dirname(dest_path)
    if dir:
        os.makedirs(dir, exist_ok = True)
    with open(dest_path, "w") as h:
        content = h.write(template_content)

    