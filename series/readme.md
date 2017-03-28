# Recherches sur les séries

Groupe : Erna, ohaila, Nidia, Justine, Mathilde

Corpus sur les séries, partitionnement selon les notes, 3 catégories :
- négatif : 1 à 3
- neutre : 4 à 7
- positif : 8 à 10

## Spécificités

### Remarques générales

"nous" est représentatif du corpus positif.

### Les personnages et acteurs

On parle des personnages si la série est pas mal et des acteurs si la série est bonne.

On constate avec les expresisons régulières que la recherche de type EN+est+ADJ renvoie des phrases sur les acteurs et personnages et on obtient principalement des adjectifs positifs. C'est une spécificité des critiques positives se référants aux acteurs.

cooccurrences de ‘principal’ : personnage, acteur, jeu, grand, bonne, super, rôle, intérêt, charisme.

La liste des coocurrents de "principal" confirment que "principal" se rapporte presque exclusivement au "personnage" ou à l'"acteur" principal et les premiers coocurrents sont des mots positifs, on peut affirmer que parler des "acteurs" et des "personnages" est synonyme d'une critique positive, notamment quand on parle des "acteurs".


### Musique et Bande son



## Taglines (phrases d'accroches)


## Recherche REGEX

1) [frpos="NAM"]+[word=".*"][frpos="ADV" & word=".*ment"][word=".*"]{1,5}
2) [word="[A-Z][a-z]+"]+[word="est"][word=".*"]+
3) [word="[A-Z][a-z]+"]+[word="est"][word=".*"]?[frpos="ADJ"]
