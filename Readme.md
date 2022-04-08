# Hugo Website

## Start server

```bash
cd hugowebsite
hugo server
```


## What to do ? 

 - change config: config.toml
 - change images in static/img/


# how to get the content ?

```bash
git clone https://github.com/sharty8/hugowebsite.git
cd hugowebsite/
```

And when you are done with your changes, push it back to github.
```bash
hugo && \
mv public docs && \
git add --all && \
git commit -m "new commit" && \
git push origin/master
```
