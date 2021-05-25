# Creating a new Video Post

1. Upload video to youtube as unlisted or public.
2. Copy below format of md into a new file and modify title, date, category and video url:

```
Title: Surah Yusuf, Verse 18
Date: 2021-01-08 10:20
Category: Surah Yusuf

Are finders keepers? Lets find out. Get it? "Find" out? :)

<iframe width="560" height="315" src="https://www.youtube.com/embed/jY4HZwTNXMw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

3. Save it in content folder as a .md file.
4. publish by running command from the root directory in a terminal: `pelican`
5. run `cd output`
6. run `python3 -m http.server` to preview your local website.
7. Browse to localhost:8000


# For future knowledge

unpaid format for keeping domain through github
`SITEURL = 'https://<gitUserName>.github.io/<repoName>'`

---------

# Rebuild website when working on it
Run command `pelican -r` from the main folder (source)

docs is your deployed - prod 
output is your local

# Publish to docs directory
Rename by deleting docs and renaming output to docs.
- Run command from main project folder: 

```
    rm -rf docs
    mv output docs 

```

# How to run in your local browser
Run from the output directory: 
`python3 -m http.server`

View at http://localhost:8000

# To do:

- Create category/ Learn it. (created review)
- Find a good theme/ colours
- Show sparkles on arrival
- fix links and socials
- Upload ALL recordings

