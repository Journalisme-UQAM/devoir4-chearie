# coding : utf-8

import csv, spacy
from collections import Counter

tal = spacy.load("fr_core_news_md")
tal.Defaults.stop_words.add("y")
tal.Defaults.stop_words.add("t")
tal.Defaults.stop_words.add("il")
tal.Defaults.stop_words.remove("gens")

martino = "martino.csv"

f = open(martino)
mots = csv.reader(f)
next(mots)

tousMots = []
motsFiltres = []

for mot in mots:
    # print(mot[3]) J'ai bien imprimé tous les mots que Martineau a écrit. 
    corr = tal(mot[3])
    # for token in corr:
    #     print(token.text)
    lemmes = [token.lemma_ for token in corr if token.is_stop == False and token.is_punct == False]
    # print(lemmes)
    for words in lemmes:
            # print(word)
        for x,y in enumerate(lemmes[:-1]):
            if "islam" in words:
                motsFiltres.append("{} {}".format(lemmes[x],lemmes[x+1]))
            elif "musulm" in words:
                motsFiltres.append("{} {}".format(lemmes[x],lemmes[x+1]))

freq = Counter(motsFiltres)
print(freq.most_common(50))