import random
def jeu_lance_des():
    for nb_essais in range(0,3):
        print("Lancez les dés en appuyant sur 'Entrée'")
        saisie=input()
        if saisie=="":
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            des_joueur = (a, b)
            print(des_joueur)
            if 6 in des_joueur:
                print("Vous remportez la partie et la clé.")
                return True
            if nb_essais<1:
                print("Il vous reste", 3 - nb_essais - 1, "essais")
            else:
                print("Il vous reste un essai")
            print("Au tour du maître du jeu")
            c = random.randint(1, 6)
            d = random.randint(1, 6)
            des_maitre = (c, d)
            print(des_maitre)
            if 6 in des_maitre:
                print("Le maître du jeu remporte la partie et vous perdez la clé.")
                return False
    print("Après trois essais, aucun des joueurs n'a gagné, c'est donc un match nul.")

def bonneteau() :
    import random
    L = ["A", "B", "C"]


    n=2
    clef=random.choice(L)
    print("Sous quel bonneteau se trouve la clef ? vous avez 2 tentatives")
    t=str(input("Choisissez un bonneteau A,B ou C: "))

    while t!=clef:
        n=n-1
        if n == 0:
            print("Vous avez perdu !")
            return False
        print("La clef ne se trouve pas ici, il vous reste", n, "tentatives")

        t=str(input("Choisissez un autre bonneteau: "))


    if t==clef:
        print("Bravo vous obtenez la clef")
        return True
epreuveshasard=[jeu_lance_des,bonneteau]
def epreuve_hasard():
    epreuve = random.choice(epreuveshasard)
    return epreuve()
