# convert the json files we downloaded to csv, to be able to be annotated

import json
import csv
import os
import argparse

def convert_to_tsv(filename):
    with open(filename) as f:
        data = json.load(f)
    with open(f"{os.path.splitext(filename)[0]}.tsv", 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['title', 'content'])
        for article in data['articles']:
            # make sure there's no newline, tab, carriage return in the content
            article['content'] = article['content'].replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
            writer.writerow([article['title'], article['content']])
    print(f"Converted {filename} to {os.path.splitext(filename)[0]}.tsv")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The name of the json file to convert")
    args = parser.parse_args()

    convert_to_tsv(args.filename)