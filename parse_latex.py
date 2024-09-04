from TexSoup import TexSoup

# Load and parse the LaTeX document
with open(r'C:\Users\nisha\Downloads\sample.tex', 'r') as file:
    latex_doc = file.read()

soup = TexSoup(latex_doc)

def format_content(content):
    """Format the content to strip extra whitespace and handle lists."""
    if isinstance(content, list):
        return ' '.join(item.strip() for item in content if item.strip())
    elif isinstance(content, str):
        return content.strip()
    return content

def print_tex_node(node):
    """Print the LaTeX node type and its formatted content."""
    if hasattr(node, 'name'):
        content = format_content(node.text)
        if content:
            print(f"Node Type: {node.name}")
            print(f"Content:\n{content}\n")
        else:
            print(f"Node Type: {node.name}\nNo content.\n")
    else:
        print(f"Other Type: {type(node)}\nContent:\n{node}\n")

def process_tex_document(soup):
    """Process and print the LaTeX document content."""
    for item in soup:
        if item.name in ['documentclass', 'usepackage']:
            print_tex_node(item)

        elif item.name == 'document':
            print("\nDocument Content:")
            print_tex_node(item)

        elif item.name == 'itemize':
            print("\nList of items:")
            for subitem in item.find_all('item'):
                print(f"- {subitem.text.strip()}")

        elif item.name in ['eqnarray', 'equation']:
            print("\nEquation:")
            print(format_content(item.text))

        elif item.name == 'figure':
            caption = item.find('caption').text if item.find('caption') else 'No caption'
            label = item.find('label').text if item.find('label') else 'No label'
            print(f"\nFigure Caption: {caption}")
            print(f"Figure Label: {label}")

# Process the document
process_tex_document(soup)
