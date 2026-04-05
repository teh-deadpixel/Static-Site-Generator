def markdown_to_blocks(markdown):
    splitted = markdown.split("\n\n")
    stripped = []
    for st in splitted:
        strip = st.strip()
        if strip == "":
            continue
        stripped.append(strip)
    return stripped