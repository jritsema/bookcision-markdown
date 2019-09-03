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
        lastHighlight = highlights[len(highlights)-1]["location"]["value"]

        for h in highlights:
            markdown += f"{h['location']['value']} of {lastHighlight}\n\n"
            if h["note"]:
                markdown += f"**{h['note']}**\n\n"
            markdown += f"> {h['text']}\n\n"

    # write output
    with open(output, 'w') as outfile:
        outfile.write(markdown)


if __name__ == "__main__":
    main()
