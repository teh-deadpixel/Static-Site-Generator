from textnode import TextNode
from textnode import TextType
import os
import shutil
from gencontent import generate_pages_recursive

def copy_static(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for entry in os.listdir(source):
        destination_path = os.path.join(destination, entry)
        source_path = os.path.join(source, entry)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"file copied: {destination_path} from {source_path}")
        else:
            copy_static(source_path, destination_path)


def main():
    #node =  TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(node)
    source = "static"
    destination = "public"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy_static(source, destination)
    generate_pages_recursive("content", "template.html", "public")
main()

