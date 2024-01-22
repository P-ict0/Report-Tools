import sys
import os
import urllib.parse
import argparse

class tocGenerator():
    def __init__(self, dirname: str, ignore_hidden: bool = False, url_encode: bool = False) -> None:
        self.dirname = dirname
        self.ignore_hidden = ignore_hidden
        self.url_encode = url_encode

    def generate(self) -> None:
        tree = self.create_tree()
        print("\n".join(tree))

    def create_tree(self) -> list[str]:
        contents = []
        for root, dirs, filenames in os.walk(self.dirname):
            if self.ignore_hidden:
                # Ignore hidden directories
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                # Ignore hidden files
                filenames[:] = [f for f in filenames if not f.startswith('.')]

            level = root.replace(self.dirname, '').count(os.sep)
            subindent = '  ' * (level)
            for file in filenames:
                file_path = os.path.relpath(os.path.join(root, file), self.dirname).replace("\\","/")

                # Url encode the file path
                if self.url_encode:
                    file_path = urllib.parse.quote(file_path)

                # Remove file extension from link text
                link_text = os.path.splitext(file)[0]
                contents.append(f'{subindent}- [{link_text}]({file_path})')

        return contents


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Generate Contents with links to files of a given directory')
    parser.add_argument('--ignore-hidden', '--ih', action='store_true', help='Ignore hidden files and directories')
    parser.add_argument('--url-encode', '--ue', action='store_true', help='Url encode the file path')
    parser.add_argument('dirname', type=str, help='Directory to generate contents for')
    args = parser.parse_args()

    toc = tocGenerator(args.dirname, args.ignore_hidden, args.url_encode)
    toc.generate()
