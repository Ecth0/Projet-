import json
import random

def charge_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def enigme_pere_fouras():
    data=charge_enigmes('data/enigmesPF.json')
    enigmeschoisie = random.choice(data)
    print("Voici l'énigme du père Fouras :")
    print(enigmeschoisie["question"])
    n = 3

    while n > 0:
        n = n - 1
        reponse_user = str(input())
        if reponse_user.lower() == (enigmeschoisie["reponse"].lower()):
            print("C'est ça ! Vous gagnez la clé.")
            return True
        elif n == 0:
            print("Perdu")
            return False
        else:
            print("Non essayez encore , il vous reste", n, "essais ")
