# Developer Enviornment Setup

- Install Python 3.x
- Install all required pip packages: `pip install -r requirements.txt`

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

# Rebuild website when working on it
1. publish by running command from the root directory in a terminal: `pelican -r`

    docs is your deployed - prod 
    output is your local

# How to run in your local browser

Run from the output directory: 
`python3 -m http.server`

View at http://localhost:8000

# Publish to docs directory
Rename by deleting docs and renaming output to docs.
- Run command from main/root project folder: 

```
    rm -rf docs
    mv output docs 
    copy CNAME docs

```

# Test production version of code

Run from the docs directory: 
`python3 -m http.server`

# Final Step: Commit docs folder to push to production

`git commit -a -m "video added xyz"`
`git push`

# To do:

- Create category/ Learn it. (created review)
- Find a good theme/ colours
- Show sparkles on arrival
- fix links and socials
- Upload ALL recordings




# For future knowledge

unpaid format for keeping domain through github
`SITEURL = 'https://<gitUserName>.github.io/<repoName>'`

