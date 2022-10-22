#!/usr/bin/env python3

import markdown
import os
import shutil

from re import sub

from sys import argv
from pathlib import Path

# slash = "/"

# if os.name == "nt":
#     slash = "\\"

# Helper functions

def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data


class Document():
    def __init__(self, path):
        self.path = path
        self.outpath = sub("..$", "html", path)
        with open(path, 'r') as f:
            md = markdown.Markdown(extensions = ['meta'])
            self.raw = f.read()
            self.html = md.convert(self.raw)
            self.meta = md.Meta

    def generate_page(self):
        if "template" not in self.meta:
            print(f"Template Not specified for {path}")
            return
        if "title" not in self.meta:
            print(f"Title not specified for {path}")
            return

        template_name = f"templates/{self.meta['template'][0]}.html"
        template_html = Path(template_name).read_text()

        print(template_html)

        final_html = sub("{title}", self.meta["title"][0], template_html)
        final_html = sub("{content}", self.meta["title"][0], template_html)

        print(final_html)




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


    for doc in docs:
        os.remove(doc.path)
        doc.generate_page()








def main():
    if argv[-1] == "start":
        start()
    if argv[-1] == "build":
        build()


main()
