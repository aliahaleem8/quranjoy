#!/usr/bin/env python
from pytube import YouTube
import json

import os
import time

DATA_FILENAME = "urls.json"
IFRAME_CONTENT = '<iframe width="650" height="365" src="{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
TEMPLATE_MARKDOWN = "Title: {title}\nDate: {date}\nCategory: {category}\n\n{content}"
OUTPUT_DIRECTORY = "generated"

def read_json_data():
    with open(DATA_FILENAME) as file_handle:
        content = file_handle.read()
        return json.loads(content)

def generate_data(urls, category):
    for url in urls:

        youtube_data = YouTube(url)
        title = youtube_data.title
        published_date = youtube_data.publish_date
        
        iframe_content = IFRAME_CONTENT.format(url)
        content = TEMPLATE_MARKDOWN.format(title = title, date = published_date, category = category, content = iframe_content)

        clean_filename = title.replace(' ', '-') \
            .replace('(', '').replace(')', '').replace(',', '') \
            .replace('--', '-')

        filename = "{}.md".format(clean_filename)

        with open("{}/{}".format(OUTPUT_DIRECTORY, filename), "w") as file_handle:
            content = file_handle.write(content)

def main():
    start_time = time.time()
    json_data = read_json_data()

    if not os.path.isdir(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

    urls = json_data["urls"]
    category = json_data["category"]

    if len(category) < 0:
        print("Please enter a category in {}".format(DATA_FILENAME))
        exit(1)

    print("Processing {} videos ...".format(len(urls)))
    generate_data(urls, category)

    end_time = time.time()
    elapsed_seconds = end_time - start_time
    print("Done in {}s".format(len(urls), elapsed_seconds))

main()