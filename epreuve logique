import random  # Importation de la bibliothèque random pour les choix aléatoires

def grille_vide():  # Fonction qui crée une grille vide 3x3
    grillevide=[]  # Initialisation de la liste qui va contenir la grille
    for i in range(3):  # Boucle pour chaque ligne
        L = []  # Liste pour chaque ligne
        for j in range(3):  # Boucle pour chaque colonne
            L.append(" ")  # Ajout d'un espace vide pour chaque colonne
        grillevide.append(L)  # Ajout de la ligne à la grille
    return grillevide  # Retour de la grille vide

def suiv(joueur):  # Fonction pour alterner entre les joueurs
    if joueur == 1:  # Si le joueur actuel est 1
        return joueur - 1  # Le joueur suivant est 0
    else:
        return 1  # Sinon, le joueur suivant est 1

ac="abc"  # Variable inutilisée, probablement une erreur ou du code résiduel

def affiche_grille(grille, message):  # Fonction pour afficher la grille de jeu
    #print(message)  # Affichage de l'éventuel message (commenté)
    for i in range(3):  # Boucle pour chaque ligne
        for j in range(3):  # Boucle pour chaque colonne
            print("|", grille[i][j], end=" ")  # Affichage de chaque case avec un séparateur vertical
            if j == 2:  # Si c'est la dernière colonne
                print("|", end="")  # Affichage du séparateur vertical à la fin de la ligne
        print("")  # Passage à la ligne suivante
    print("-------------")  # Affichage de la séparation entre les lignes de la grille

def demande_position():  # Fonction pour demander une position valide à l'utilisateur
    a, b, c = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) :")  # Demande d'entrée
    while True:  # Boucle jusqu'à ce que la position soit valide
        if not (1 <= int(a) <= 3) or not (1 <= int(c) <= 3) or b != ",":  # Vérification de la validité
            a, b, c = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) :")  # Redemande si invalide
        else:
            return a, b, c  # Retourne les valeurs si elles sont valides

def init():  # Fonction pour initialiser les positions des bateaux du joueur
    grillejoueur = grille_vide()  # Création de la grille vide
    print("Positionnez vos bateaux :")  # Message pour l'utilisateur
    print("Bateau 1")  # Demande de la première position du bateau
    pos1l = "0"  # Initialisation de la position du bateau
    pos1c = "0"
    _ = '0'
    while (int(pos1l) < 1 or int(pos1l) > 3) or (int(pos1c) < 1 or int(pos1c) > 3) or _ != ",":  # Vérification de la position
        pos1l, _, pos1c = input(("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2)"))  # Demande de la position
    grillejoueur[int(pos1l) - 1][int(pos1c) - 1] = "B"  # Place le premier bateau
    print("Bateau 2")  # Demande de la deuxième position du bateau
    pos2l = "0"
    pos2c = "0"
    _ = '0'
    while (int(pos2l) < 1 or int(pos2l) > 3) or (int(pos2c) < 1 or int(pos2c) > 3) or _ != "," or (pos2l == pos1l and pos2c == pos1c):  # Vérification de la position, évite la répétition
        pos2l, _, pos2c = input(("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2)"))  # Demande de la position
    grillejoueur[int(pos2l) - 1][int(pos2c) - 1] = "B"  # Place le deuxième bateau
    print("Découvrez votre grille de jeu avec vos bateaux :")  # Affiche la grille après placement des bateaux
    affiche_grille(grillejoueur, _)  # Affichage de la grille avec les bateaux
    return grillejoueur  # Retourne la grille avec les bateaux placés

_ = "a"  # Variable inutilisée

def tour(joueur, grille_tirs_joueur, grilleadversaire, tirs_possible):  # Fonction pour jouer un tour
    if joueur == 0:  # Si c'est au joueur de jouer
        print("C'est à votre tour de faire feu !")  # Message indiquant que c'est le tour du joueur
        #grilleadversaire = grillemaitre  # (Commenté, probablement du code résiduel)
        print("Rappel de l'historique des tirs que vous avez effectués :")  # Affichage de l'historique des tirs
        affiche_grille(grille_tirs_joueur, _)  # Affichage de la grille des tirs du joueur
        l = "0"
        a = "0"
        c = "0"
        while (int(l) < 1 or int(c) < 1 or int(c) > 3) or (a != ","):  # Vérification de la position de tir
            l, a, c = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) :")  # Demande de la position de tir
        if grilleadversaire[int(l) - 1][int(c) - 1] == "B":  # Si un bateau est touché
            print("Touché coulé")  # Message de touche
            grille_tirs_joueur[int(l) - 1][int(c) - 1] = "x"  # Marque le bateau touché sur la grille
        else:
            print("Dans l'eau...")  # Message si le tir ne touche rien
            grille_tirs_joueur[int(l) - 1][int(c) - 1] = "."  # Marque le tir manqué
    elif joueur == 1:  # Si c'est au maître du jeu de jouer
        print("C'est le tour du maître du jeu :")  # Message indiquant que c'est au maître du jeu
        idx = random.randint(0, len(tirs_possible) - 1)  # Choix aléatoire d'une position pour le tir
        posit = tirs_possible[idx]  # Récupération de la position
        l2, c2 = posit  # Extraction de la ligne et colonne de la position
        print("Le maître du jeu tire en position :", l2, ",", c2)  # Affichage de la position du tir
        if grilleadversaire[l2 - 1][c2 - 1] == "B":  # Si le tir touche un bateau
            print("Touché coulé !")  # Message de touche
            grille_tirs_joueur[l2 - 1][c2 - 1] = "x"  # Marque le bateau touché sur la grille
        else:
            print("Dans l'eau...")  # Message si le tir ne touche rien
            grille_tirs_joueur[l2 - 1][c2 - 1] = "."  # Marque le tir manqué
        del(tirs_possible[idx])  # Retire cette position des tirs possibles

def gagne(grille_tirs):  # Fonction pour vérifier si un joueur a gagné
    compteur = 0  # Compteur de touches
    for i in range(len(grille_tirs)):  # Parcours de la grille
        for j in range(len(grille_tirs)):  # Parcours des cases de la grille
            if grille_tirs[i][j] == "x":  # Si une case est marquée comme touchée
                compteur += 1  # Incrémente le compteur
    if compteur == 2:  # Si deux bateaux sont coulés
        return True  # Le joueur a gagné
    return False  # Sinon, la partie continue

def jeu_bataille_navale():  # Fonction pour gérer le jeu de la bataille navale
    a = False  # Initialisation de l'état de fin de jeu
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")  # Message explicatif
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. ")  # Légende
    print("Les bateaux coulés sont marqués par 'x'.")  # Légende
    grillejoueur = init()  # Initialisation de la grille du joueur
    grillemaitre = grille_vide()  # Initialisation de la grille du maître
    grille_tirs_joueur = grille_vide()  # Initialisation de la grille des tirs du joueur
    grille_tirs_maitre = grille_vide()  # Initialisation de la grille des tirs du maître
    grillemaitre[random.randint(0, 2)][random.randint(0, 2)] = "B"  # Placement aléatoire du premier bateau du maître
    grillemaitre[random.randint(0, 2)][random.randint(0, 2)] = "B"  # Placement aléatoire du deuxième bateau du maître
    joueur = 1  # Le maître commence
    tirs_possible = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]  # Positions possibles de tirs
    while a == False:  # Tant que le jeu n'est pas terminé
        if suiv(joueur) == 0:  # Si c'est le tour du joueur
            tour(0, grille_tirs_joueur, grillemaitre, tirs_possible)  # Le joueur tire
            joueur = 0  # Le joueur passe son tour
            a = gagne(grille_tirs_joueur)  # Vérifie si le joueur a gagné
        else:
            tour(1, grille_tirs_maitre, grillejoueur, tirs_possible)  # Le maître tire
            joueur = 1  # Le maître passe son tour
            a = gagne(grille_tirs_maitre)  # Vérifie si le maître a gagné
    if gagne(grille_tirs_maitre) == True:  # Si le maître a gagné
        print("Le maître remporte la partie. Vous perdez la clé.")  # Affichage de la défaite du joueur
        return False  # Retourne False pour signaler la défaite
    else:
        print("Vous gagnez la clé.")  # Affichage de la victoire du joueur
        return True  # Retourne True pour signaler la victoire du joueur

def affiche_batonnets(n):  # Affiche les bâtonnets restants
    listebat = []  # Liste des bâtonnets restants
    listebat.append(n * "|")  # Affiche les bâtonnets sous forme de barres "|"
    print("Bâtonnets restants:", listebat[0])  # Affiche les bâtonnets restants

def joueur_retrait(n):  # Demande au joueur combien de bâtonnets il veut retirer
    print("Tour du joueur.")  # Affiche que c'est au tour du joueur
    retrait = int(input("Combien de bâtonnets voulez-vous retirer (1, 2 ou 3) ?"))  # Demande de retrait
    return retrait  # Retourne le nombre de bâtonnets retirés

def maitre_retrait(n):  # Logique pour le maître qui retire des bâtonnets
    if n % 4 == 1:  # Si le nombre de bâtonnets restants est congruent à 1 mod 4
        retrait = 1  # Le maître retire 1 bâtonnet
    elif n % 4 == 2:  # Si le nombre de bâtonnets restants est congruent à 2 mod 4
        retrait = 2  # Le maître retire 2 bâtonnets
    else:
        retrait = 3  # Sinon, il retire 3 bâtonnets
    return retrait  # Retourne le nombre de bâtonnets retirés

def jeu():  # Fonction pour jouer au jeu des bâtonnets
    n = 20  # Initialisation du nombre de bâtonnets
    tour = True  # Le premier tour est celui du joueur
    affiche_batonnets(n)  # Affichage des bâtonnets restants
    while n != 0:  # Tant qu'il reste des bâtonnets
        if tour == True:  # Si c'est au tour du joueur
            retrait = joueur_retrait(n)  # Le joueur retire des bâtonnets
            n = n - retrait  # Mise à jour du nombre de bâtonnets
            affiche_batonnets(n)  # Affichage des bâtonnets restants
        else:  # Si c'est au tour du maître du jeu
            retrait = maitre_retrait(n)  # Le maître retire des bâtonnets
            n = n - retrait  # Mise à jour du nombre de bâtonnets
            print("Le maître du jeu retire", retrait, "bâtonnets.")  # Affichage du retrait du maître
            affiche_batonnets(n)  # Affichage des bâtonnets restants
        if n == 0 and tour == True:  # Si le joueur a retiré le dernier bâtonnet
            print("Vous avez retiré le dernier bâtonnet, vous perdez la clé.")  # Le joueur perd
            return False  # Retourne False pour signaler la défaite du joueur
        elif n == 0 and tour == False:  # Si le maître a retiré le dernier bâtonnet
            print("Le maître du jeu a retiré le dernier bâtonnet. Le joueur gagne !")  # Le joueur gagne
            return True  # Retourne True pour signaler la victoire du joueur
        if tour == False:  # Si c'est au tour du maître
            tour = True  # Le tour suivant est celui du joueur
        else:
            tour = False  # Sinon, c'est au tour du maître

epreuveslogique = [jeu_bataille_navale, jeu]  # Liste des épreuves possibles

def epreuve_logique():  # Fonction pour sélectionner aléatoirement une épreuve logique
    epreuve = random.choice(epreuveslogique)  # Choix aléatoire dans la liste
    return epreuve()  # Appel de l'épreuve sélectionnée

