import sys
import os
import urllib.parse

def main(dirname: str) -> None:
    tree = generate_tree(dirname)
    print("\n".join(tree))

def read_dir(dirname: str) -> list[str]:
    files = []
    for root, dirs, filenames in os.walk(dirname):
        for file in filenames:
            file_path = os.path.relpath(os.path.join(root, file), dirname)
            files.append(file_path)
    return files

def print_tree(tree: list[str]) -> str:
    return '\n'.join(tree)

def generate_tree(dirname: str) -> list[str]:
    contents = []
    for root, dirs, filenames in os.walk(dirname):
        # Ignore hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        # Ignore hidden files
        filenames[:] = [f for f in filenames if not f.startswith('.')]

        level = root.replace(dirname, '').count(os.sep)
        subindent = '  ' * (level)
        for file in filenames:
            file_path = os.path.relpath(os.path.join(root, file), dirname).replace("\\","/")

            # Url encode the file path
            processed_file_path = urllib.parse.quote(file_path)

            # Remove file extension from link text
            link_text = os.path.splitext(file)[0]
            contents.append(f'{subindent}- [{link_text}]({processed_file_path})')

    return contents


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 create-markdown-file-tree.py <dirname>')
        sys.exit(1)

    dirname = sys.argv[1]
    main(dirname)
