import random
def salle_De_tresor():
    import json
    with open('data/indicesSalle.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)
        annee=random.choice(list(jeu_tv["Fort Boyard"].keys()))
        emission=random.choice(list(jeu_tv["Fort Boyard"][annee].keys()))
        indices=(list(jeu_tv["Fort Boyard"][annee][emission]["Indices"]))
        mot_code=jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]
        for i in range(0,3):
            print("L'indice numéro",i+1,"est",indices[i])
        nombre_essais=3
        a=1
        reponse_correcte=False
        while nombre_essais>0:
            print("Qui suis-je?: ")
            reponse=input()
            if reponse.lower()==mot_code.lower():
                reponse_correcte=True
                break
            else:
                nombre_essais-=1
                if nombre_essais>1:
                    print("Il vous reste",nombre_essais,"essais.")
                    print(indices[3+a])
                elif nombre_essais==1:
                    print("Il vous reste",nombre_essais,"essai.")
                    print(indices[3 + a])
                else:
                    print("La réponse était:",mot_code)
                a+=1
        if reponse_correcte==True:
            print("La réponse était bien",mot_code.lower(),"vous avez gagné!")
            print("Vous remportez la victoire !!!")
