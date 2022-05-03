# Hugo Website

## Start server

```bash
hugo server
```

## Create an article

```bash
hugo new
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
hugo || echo FAILED HUGO BUILD && \
rm -rf docs || echo FAILED RM DOCS && \
mv public docs || echo FAILED MV DOCS && \
git add --all && \
git commit -m "new commit" && \
git push
```
