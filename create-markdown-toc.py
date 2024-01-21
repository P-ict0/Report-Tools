import re

def main(filename: str) -> str:
    with open(filename, 'r') as f:
        lines = f.readlines()

    toc = generate_toc(lines)

    return '\n'.join(toc)


def generate_toc(lines: list[str]) -> list[str]:
    toc = []
    inside_code_block = False

    for line in lines:
        if line.startswith('```'):
            inside_code_block = not inside_code_block  # Toggle the code block flag
        elif not inside_code_block and line.startswith('#'):
            # Determine heading level and title
            heading_level = line.count('#')
            title = line[heading_level:].strip()

            # Generate the corresponding indentation for the toc
            indentation = '    ' * (heading_level - 1) if heading_level > 1 else ''

            processed_title = re.sub(r'[^\w\s]', '', title).lstrip().lower().replace(' ', '-').replace('--', '-')

            toc.append(f'{indentation}- [{title}](#{processed_title})')

    return toc


if __name__ == '__main__':
    filename = r'filename'
    result = main(filename)
    print(result)

