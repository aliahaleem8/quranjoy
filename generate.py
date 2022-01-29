#!/usr/bin/env python
from pytube import YouTube
import json

import os
import time

DATA_FILENAME = "urls.json"
IFRAME_CONTENT = '<iframe width="650" height="365" src="{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
TEMPLATE_MARKDOWN = "Title: {title}\nDate: {date}\nCategory: {category}\n\n{content}\n{description}"
OUTPUT_DIRECTORY = "generated"

def read_json_data():
    with open(DATA_FILENAME) as file_handle:
        content = file_handle.read()
        return json.loads(content)

def generate_data(data_list):
    for item in data_list:
        # Pytube imported and utlized:
        # Searched google for "pytube scrap"; 
        # Discovered "YouTube" function that exposes details from youtube videos (such as tilte, date, etd)"
        #
        url = item["url"] # item["url"]
        category = item["category"]
        published_date =  item["date"]  #youtube_data.publish_date
        tags = item["tags"] # not used yet
        attachments = item["attachments"] # not used yet

        # Get the data for the markdown file
        youtube_data = YouTube(url) 
        title = youtube_data.title
        description = youtube_data.description
        
        iframe_content = IFRAME_CONTENT.format(url)
        content = TEMPLATE_MARKDOWN.format(title = title, date = published_date, description = description, category = category, content = iframe_content)

        # Clean up and specify the filename
        clean_filename = title.replace(' ', '-') \
            .replace('(', '').replace(')', '').replace(',', '') \
            .replace('--', '-').replace('|', '')

        filename = "{}.md".format(clean_filename)

        # Write the markdown output
        with open("{}/{}".format(OUTPUT_DIRECTORY, filename), "w") as file_handle:
            content = file_handle.write(content)

def main():
    start_time = time.time()
    json_data = read_json_data()

    if not os.path.isdir(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

    urls = json_data["urls"]
    print("Processing {} videos ...".format(len(urls)))
    generate_data(urls)

    end_time = time.time()
    elapsed_seconds = end_time - start_time
    print("Done in {}s".format(len(urls), elapsed_seconds))

main()