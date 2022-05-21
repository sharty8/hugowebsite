# Hugo Website

## Start server

```bash
hugo server
```

# how to get the content ?

And when you are done with your changes, push it back to github.
```bash
hugo || echo FAILED HUGO BUILD && \
rm -rf docs || echo FAILED RM DOCS && \
mv public docs || echo FAILED MV DOCS && \
git add --all && \
git commit -m "new commit" && \
git push
```
