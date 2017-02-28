#!/usr/bin/env python3
# coding=utf-8

import requests
import argparse
import re
import json
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("categorie",
                    help="La catégorie dont il faut extraire les oeuvres",
                    choices=["films", "series", "jeux", "livres", "bd",
                             "musique"])
parser.add_argument("seuilAvis",
                    help="Le nombre d'avis' à partir de laquelle une\
                          oeuvre est récupérée.",
                    type=int)
parser.add_argument("seuilOeuvres",
                    help="Le nombre d'oeuvre à récupérer",
                    type=int)
args = parser.parse_args()


def main():
    corpus = dict()
    pattern = re.compile("    *if \(typeof sas !== 'undefined'\) {\n    *sas.render\('\d+'\);\n    *}\n    *")
    pageN = 1
    nbOeuvres = 0
    while nbOeuvres < args.seuilOeuvres:
        requete = requests.get("https://www.senscritique.com/" +
                               args.categorie + "/oeuvres/page-" +
                               str(pageN)).content
        oeuvresSoup = BeautifulSoup(requete)
        oeuvres = oeuvresSoup.find_all("a", {"class": "erra-global"})
        for oeuvre in oeuvres:
            if nbOeuvres >= args.seuilOeuvres:
                break
            # print(a)
            nbAvis = oeuvre.attrs['title']
            # print(title)
            nbAvis = nbAvis.replace("Note globale pondérée sur : ", "")
            nbAvis = nbAvis.replace(" avis", "")
            nbAvis = int(nbAvis)
            # print(nbAvis)
            if nbAvis >= args.seuilAvis:
                fiche = oeuvre.attrs['href']
                requete = requests.get("https://www.senscritique.com/" +
                                       fiche + "#page-1/filter-all/").content
                ficheSoup = BeautifulSoup(requete)
                titreOeuvre = ficheSoup.find("span",
                                             {"class": "d-heading1 d-cover-title pco-cover-title"}).getText()
                if titreOeuvre not in corpus:
                    print("Récupération des critiques pour " + titreOeuvre)
                    corpus[titreOeuvre] = dict()
                    nbOeuvres += 1
                    critiques = ficheSoup.find_all("a",
                                                   {"class": "ere-review-anchor"})
                    for critique in critiques:
                        critiqueURL = critique.attrs['href']
                        requete = requests.get("https://www.senscritique.com/" +
                                               critiqueURL).content
                        critiqueSoup = BeautifulSoup(requete)
                        # print(critiqueSoup)
                        utilisateur = "".join(critiqueSoup.find("a", {"class": "rvi-header-author"}).getText().split())
                        if utilisateur not in corpus[titreOeuvre]:
                            # print("Récupération de la critique de " + utilisateur)
                            corpus[titreOeuvre][utilisateur] = dict()
                            date = critiqueSoup.find("time",
                                                     {"class": "rvi-review-release"}).attrs['datetime']
                            corpus[titreOeuvre][utilisateur]['date'] = date
                            note = int("".join(critiqueSoup.find("span", {"itemprop": "ratingValue"}).getText().split()))
                            corpus[titreOeuvre][utilisateur]['note'] = note
                            critiqueContenu = critiqueSoup.find("div",
                                                                {"class": "rvi-review-content"}).getText()
                            critiqueContenu = pattern.sub("", critiqueContenu)
                            corpus[titreOeuvre][utilisateur]['critique'] = critiqueContenu
                            print(" | ".join([titreOeuvre,utilisateur,date,str(note)]))
                            # print(corpus[titreOeuvre][utilisateur]['critique'])
                            # print(critiqueCorps)
                            # print("-------------------")
                    # print(soup)
                    # print (ficheSoup)
                    topMenu = ficheSoup.find("div",
                                             {"class": "eipa-interface eipa-top"})
                    if topMenu is not None:
                        pages = topMenu.find_all("a", "eipa-anchor")
                        for page in pages:
                            # print(page)
                            pageURL = page.attrs['href']
                            requete = requests.get("https://www.senscritique.com/" +
                                                   pageURL).content
                            pageSoup = BeautifulSoup(requete)
                            critiques = pageSoup.find_all("a",
                                                          {"class": "ere-review-anchor"})
                            for critique in critiques:
                                critiqueURL = critique.attrs['href']
                                requete = requests.get("https://www.senscritique.com/" +
                                                       critiqueURL).content
                                critiqueSoup = BeautifulSoup(requete)
                                # print(soup)
                                utilisateur = "".join(critiqueSoup.find("a", {"class": "rvi-header-author"}).getText().split())
                                if utilisateur not in corpus[titreOeuvre]:
                                    corpus[titreOeuvre][utilisateur] = dict()
                                    corpus[titreOeuvre][utilisateur]['date'] = critiqueSoup.find("time",
                                                                        {"class": "rvi-review-release"}).attrs['datetime']
                                    corpus[titreOeuvre][utilisateur]['note'] = int("".join(critiqueSoup.find("span", {"itemprop": "ratingValue"}).getText().split()))
                                    critiqueContenu = critiqueSoup.find("div",
                                                                        {"class": "rvi-review-content"}).getText()
                                    corpus[titreOeuvre][utilisateur]['critique'] = pattern.sub("", critiqueContenu)
                                    print(" | ".join([titreOeuvre,utilisateur,date,str(note)]))
                                # print(critiqueCorps)
                                # print("-------------------")
        pageN += 1
    with open('corpus.json', 'w') as f:
        json.dump(corpus, f, sort_keys=True, indent=4)


if __name__ == '__main__':
    main()
