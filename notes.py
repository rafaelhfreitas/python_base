#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: text
text:
Anotacao geral sobre a carreira de tecnologia

$notes.py read --tag=tech
...
...
"""

__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage.")
    print(f"you must specify a subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid argument `{arguments[0]}`")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 30)

if arguments[0] == "new":
    title = arguments[1]
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:").strip(),
    ]
    # \t -tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

