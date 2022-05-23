# Hugo Website

## Start server

écris juste 'hugo server' dans le terminal. Le terminal tu le trouves dans les onglets du haut en placant la souris en haut. 

tu écris 'ls' pour savoir où tu te trouves, si tu es dans le bon dossier.

vérifie si tu as le rendu souhaité en éditant : 

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
