import re
import sys

def main(filename: str) -> str:

    toc = generate_toc(filename)
    print("\n".join(toc))

def read_file(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def generate_toc(filename: str) -> list[str]:
    toc = []
    inside_code_block = False

    lines = read_file(filename)

    for line in lines:
        if line.startswith('```'):
            inside_code_block = not inside_code_block  # Toggle the code block flag
        elif not inside_code_block and line.startswith('#'):
            # Determine heading level and title
            heading_level = line.count('#')
            title = line[heading_level:].strip()

            # Generate the corresponding indentation for the toc
            indentation = '    ' * (heading_level - 1) if heading_level > 1 else ''

            processed_title = re.sub(r'[^\w\s-]', '', title).lstrip().lower().replace(' ', '-')

            toc.append(f'{indentation}- [{title}](#{processed_title})')

    return toc


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 create-markdown-toc.py <filename>')
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)

