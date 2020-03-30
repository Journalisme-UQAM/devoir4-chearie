# coding : utf-8

### BONJOUR ARIANE
### TRÈS BON SCRIPT!
### IL NE FALLAIT AJUSTER QUE QUELQUES PETITES CHOSES.

import csv, spacy
from collections import Counter

tal = spacy.load("fr_core_news_md")
tal.Defaults.stop_words.add("y")
tal.Defaults.stop_words.add("t")
tal.Defaults.stop_words.add("il")
tal.Defaults.stop_words.remove("gens")

# martino = "martino.csv"
martino = "../martino.csv" ### JE CHANGE CETTE LIGNE SEULEMENT POUR QUE ÇA FONCTIONNE SUR MON ORDINATEUR

f = open(martino)
mots = csv.reader(f)
next(mots)

tousMots = []
motsFiltres = []

for mot in mots:
    # print(mot[3]) J'ai bien imprimé tous les mots que Martineau a écrit. 
    corr = tal(mot[3])
    # for token in corr:
    #     print(token.text) ### INTÉRESSANT ESSAI; C'EST PARFAIT DE VOIR CE QUE NOTRE SCRIPT FAIT EN IMPRIMANT QUELQUE CHOSE, PUIS EN LE METTANT ENSUITE EN COMMENTAIRES
    lemmes = [token.lemma_ for token in corr if token.is_stop == False and token.is_punct == False]
    # print(lemmes)
    # for words in lemmes: ### CETTE PREMIÈRE BOUCLE EST INUTILE ET MULTIPLIE LE NOMBRE D'OPÉRATIONS AU CARRÉ!

    ### J'INDENTE TOUT LE CODE CI-DESSOUS D'UN CRAN VERS LA GAUCHE.

            # print(word)

    ### TON CODE FONCTIONNE TRÈS BIEN!
    ### SEULEMENT, IL NE FAIT PAS CE QUI ÉTAIT DEMANDÉ. CE QUE TU FAIS POURRAIT ÊTRE ABSOLUMENT INTÉRESSANT PAR AILLEURS! C'EST JUSTE PAS CE QUE LE DEVOIR VOUS DEMANDAIT DE FAIRE :)
    ### ICI, TU FAIS DES "BIGRAMMES" AVEC TOUS LES MOTS D'UNE CHRONIQUE DE MARTINEAU DÈS QUE CELLE-CI CONTIENT UN MOT CONTENANT "ISLAM" OU "MUSULM"
    ### JE LE PLACE EN COMMENTAIRES
    # for x,y in enumerate(lemmes[:-1]):
    #     if "islam" in words:
    #         motsFiltres.append("{} {}".format(lemmes[x],lemmes[x+1]))
    #     elif "musulm" in words:
    #         motsFiltres.append("{} {}".format(lemmes[x],lemmes[x+1]))

    ### EN FAIT, JE VOUS DEMANDAIS DE NE FAIRE DES "BIGRAMMES" QU'AVEC LES MOTS QUI CONTIENNENT "ISLAM" OU "MUSULM"
    ### AINSI, LE CODE CI-DESSOUS RÉPOND DAVANTAGE À LA QUESTION
    for x,y in enumerate(lemmes[:-1]):
        # if "islam" in words: ### CE N'EST PAS DANS "WORDS" QU'IL FAUT CHERCHER SI "ISLAM" SE TROUVE, MAIS DANS LEMMES[X] ET DANS LEMMES[X+1]
        if "islam" in lemmes[x] or "islam" in lemmes[x+1]:
            motsFiltres.append("{} {}".format(lemmes[x],lemmes[x+1]))
        # elif "musulm" in words: ### IDEM ICI
        elif "musulm" in lemmes[x] or "musulm" in lemmes[x+1]:
            motsFiltres.append("{} {}".format(lemmes[x],lemmes[x+1]))

    # print(motsFiltres)

freq = Counter(motsFiltres)
print(freq.most_common(50))