#!/usr/local/bin/python3

import sys
import json


def main():

    # args
    input = sys.argv[1]
    output = sys.argv[2]

    # read input json
    with open(input) as json_file:
        data = json.load(json_file)

        title = data["title"]
        authors = data["authors"]

        # add metadata using YAML front matter
        cleansedtitle = title.replace(":", " -")
        markdown = "---\n"
        markdown += "tags: [books]\n"
        markdown += f"title: {cleansedtitle} by {authors}\n"
        markdown += "---\n\n"

        # header
        markdown += "### "
        markdown += f"{title} by {authors}\n\n"

        # highlights with notes
        highlights = data["highlights"]
        for h in highlights:

            # preserve new lines
            t = h['text']
            if t.find("     ") != -1:
                t = t.replace("     ", "\n\n")
            markdown += f"{t}\n\n"

            if h["note"]:
                markdown += f"`{h['note']}`\n\n"

    # write output
    with open(output, 'w') as outfile:
        outfile.write(markdown)


if __name__ == "__main__":
    main()
