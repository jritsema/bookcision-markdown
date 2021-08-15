#!/usr/local/bin/python3

import sys
import json


def main():

    markdown = "### "

    # args
    input = sys.argv[1]
    output = sys.argv[2]

    # read input json
    with open(input) as json_file:
        data = json.load(json_file)

        markdown += f"{data['title']} by {data['authors']}\n\n"

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
