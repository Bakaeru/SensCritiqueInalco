# Recherches sur les séries

Groupe : Erna, ohaila, Nidia, Justine, Mathilde

Corpus sur les séries, partitionnement selon les notes, 3 catégories :
- négatif : 1 à 3
- neutre : 4 à 7
- positif : 8 à 10

## Spécificités

"nous" est représentatif du corpus positif.
On parle des personnages si la série est pas mal et des acteurs si la série est bonne.
On constate avec les expresisons régulières que la recherche de type EN+est+ADJ renvoie des phrases sur les acteurs et personnages et on obtient principalement des adjectifs positifs. C'est une spécificité des critiques positives se référants aux acteurs.

## Taglines (phrases d'accroches)


## Recherche REGEX

1) [frpos="NAM"]+[word=".*"][frpos="ADV" & word=".*ment"][word=".*"]{1,5}
2) [word="[A-Z][a-z]+"]+[word="est"][word=".*"]+
3) [word="[A-Z][a-z]+"]+[word="est"][word=".*"]?[frpos="ADJ"]
