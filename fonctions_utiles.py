def composer_equipe():
    nb = int(input("Entrez le nombre de joueurs que vous souhaitez dans votre équipe:"))
    while nb>3 or nb<=0:
        print("Le nombre de joueurs de votre équipe ne doit pas dépasser 3 et doit être supérieur à 0")
        nb = int(input("Entrez le nombre de joueur que vous souhaitez dans votre équipe:"))
    cle=0
    equipeliste=[]
    leader=False
    for i in range(nb):
        joueur={}
        cle+=1
        print("Entrez le nom, la profession et si votre joueur est leader ou membre:")
        nom=input("Entrez le nom de votre joueur: ")
        profession=input("Entrez sa profession: ")
        role=input("Entrez si votre joueur est leader 0/N: ")
        while role!="0" and role!="N":
            role=input("Entrez si votre joueur est leader 0/N: ")
        if leader == True and role=="0":
            print("Votre équipe contient déjà un leader.")
            role = input(input("Entrez si votre joueur est leader 0/N: "))
        if role=="0":
            role="Leader"
            leader=True
        else:
            role="Membre"
        joueur["nom"]=nom
        joueur["profession"]=profession
        joueur["role"]=role
        joueur["cles_gagnees"]=0
        equipeliste.append(joueur)
    if leader==False:
        equipeliste[0]["role"]="Leader"
    return equipeliste


def introduction():
    print("Bienvenue à Fort Boyard Simulator.")
    print("Dans ce jeu vous devrez accomplir des épreuves afin d'accéder à la salle du trésor.")
    print("Il vous faudra terminer 3 épreuves afin d'y accéder.")
    print("Bonne chance!")

def menu_epreuves():
    print("Quel type d'épreuve souhaitez-vous effectuer?")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du hasard")
    print("4. Énigme du Père Fouras")
    n=int(input())
    num=("1",'2',"3","4")
    while str(n) not in num:
        print("Vous devez écrire un nombre entre 1 et 4")
        n=input()
    return n


#print(equipe)
def choisir_joueur(equipe):
    print("Voici la liste des joueurs :")
    for i in range(len(equipe)):
        equipe2 = equipe[i]
        print(i+1,".",equipe2["nom"],"(",equipe2["profession"],")","-",equipe2["role"])
    joueur_choisi = int(input("Entrez le numéro du joueur: "))
    while joueur_choisi < 1 or joueur_choisi > len(equipe):
        print("Numéro invalide. Veuillez réessayer.")
        joueur_choisi = int(input("Entrez le numéro du joueur: "))
    joueur_selectionne = equipe[joueur_choisi - 1]
    return joueur_selectionne

