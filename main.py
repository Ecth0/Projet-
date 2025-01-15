import fonctions_utiles as f
import epreuve_finale as f2
import epreuves_mathematiques as em
import epreuves_hasard as eh
import epreuves_logiques as el
import enigme_pere_fouras as epf
def jeu():
    f.introduction()  # Introduction du jeu
    equipe = f.composer_equipe()  # Composer l'équipe
    compteur=0
    while compteur!=3: #On vérifie le nombre de clés obtenues
        compteur=0
        for i in range(len(equipe)):
            equipea=equipe[i]
            compteur+=int(equipea["cles_gagnees"])
        if compteur==3:
            break
        num = f.menu_epreuves()  # Menu des épreuves
        choix = f.choisir_joueur(equipe)  # Choisir un joueur
        if num ==1:
            epreuve =em.epreuve_math()  # Appel de l'épreuve mathématique
            if epreuve ==True:  # Vérification si l'épreuve est réussie
                choix["cles_gagnees"] += 1  # Ajout de la clé gagnée au joueur
        elif num==2:
            epreuve=el.epreuve_logique()
            if epreuve ==True:  # Vérification si l'épreuve est réussie
                choix["cles_gagnees"] += 1  # Ajout de la clé gagnée au joueur

    # Si l'épreuve choisie est un hasard
        elif num ==3:
            epreuve =eh.epreuve_hasard()  # Appel de l'épreuve hasard
            if epreuve == True:  # Vérification si l'épreuve est réussie
                choix["cles_gagnees"] += 1  # Ajout de la clé gagnée au joueur

    # Si l'épreuve choisie est l'énigme du Père Fouras
        elif num == 4:
            epreuve=epf.enigme_pere_fouras()
            if epreuve == True:  # Vérification si l'épreuve est réussie
                choix["cles_gagnees"] += 1  # Ajout de la clé gagnée au joueur


    f2.salle_De_tresor()
jeu()
