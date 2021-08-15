#!/usr/local/bin/python3

import os
import sys
import subprocess

in_dir = sys.argv[1]
out_dir = sys.argv[2]

home = os.environ['HOME']
directory = os.fsencode(in_dir)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    prefix = "Kindle.Highlights_"
    if filename.startswith(prefix) and filename.endswith(".json"):
        input = os.path.join(in_dir, filename)
        out = filename.replace(prefix, "")
        out = out.replace(".", " ")
        out = out.replace("_", " ")
        out = out.replace(" json", ".md")
        output = os.path.join(out_dir, out)
        print(input)
        print("->")
        app = "main.py"
        subprocess.call(["python", app, input, output])
        print(output)
        print()
        continue
    else:
        continue
