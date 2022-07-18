# Hugo Website

## Start server

This is the command to launch in the terminal to try locally.
```bash
hugo server
```
Then read the content to see how to go to the website. Usually it is on http://127.0.0.1:1313 .

It should be used in bash (the terminal) in the directory `sharty.github.io`.
```bash
# This is a comment, what is after "#" is not interpreted by the terminal

pwd  # to see where we are

ls  ## to see what there is in the directory (folders starting with a "." are invisible)

cd ..  # to go one directory less deep
cd name_of_the_folder  # to go in a folder
```


## How to get the content ?

And when you are done with your changes, push it back to github.
```bash
hugo && \
git add --all && \
git commit -m "new commit" && \
git push
```


## Warning !

The articles must be in `content/blog/`.
The images must be in `static/img/`.
The sole purpose of the `docs/` folder is for Hugo.

### Every folder explained:

 - .forestry: configuration of the Forestry CMS.
 - .github: configuration of github.
 - archetype: example of how hugo should interpret the introduction of an article.
 - content: where the user (us) need to put the articles.
 - docs: content interpreted by hugo -> what will be shown on the website.
 - resources: I dont know... (^.^')
 - static: where the user (us) can put additional content such as images and code.
 - themes: this is where the base theme is.
