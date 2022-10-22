#!/usr/bin/env python3

import markdown
import os
import shutil

from sys import argv
from pathlib import Path

# slash = "/"

# if os.name == "nt":
#     slash = "\\"


class Document():
    def __init__(self, path):
        self.path = path
        with open(path, 'r') as f:
            md = markdown.Markdown(extensions = ['meta'])
            self.raw = f.read()
            self.html = md.convert(self.raw)
            self.meta = md.Meta





def start():
    if not Path('site').is_dir():
        Path('site').mkdir()
    if not Path('templates').is_dir():
        Path('templates').mkdir()

def build():
    if not Path('site').is_dir() or not Path('templates').is_dir():
        print("Either site or templates directory is missing. Try running 'sss-g start'")
        return

    if Path('output').is_dir():
        shutil.rmtree('output')

    shutil.copytree('site', 'output')

    # Now turn the markdown files into html documents
    doc_paths = []
    docs = []
    for path, currentDirectory, files in os.walk("output"):
        for file in files:
            # We will deal only with the markdown files.
            if file.endswith(".md"):
                doc_paths.append((os.path.join(path, file)))

    for path in doc_paths:
        docs.append(Document(path))





def main():
    if argv[-1] == "start":
        start()
    if argv[-1] == "build":
        build()


main()
