# Créé par Admin, le 05/12/2020 en Python 3.7
# Pendu sur console en premier lieu

import random as random
import scorelib as sco #librairie personnelle
import potence as po #affichage de la potence

restart=""

while restart=="":  #boucle pour recommencer à la fin du jeu

    lines="freg"
    compteur=0
    alea=0
    lettre=""
    reconstmot=""
    loose=0
    verif=""
    out=False
    lettredonné=""

    name=input("Comment t'appelle-tu ?") #demande pseudo
    name=" "+name

    motAtrouver=""

    with open("dico.txt") as f: #compte le nombre de ligne du fichier
        while lines!="" :
            lines = f.readline()
            compteur+=1
    #print(compteur)
    alea=random.randint(0,compteur-1) #génere un nbr aléatoire
    #print(alea)
    with open("liste_de_mots.txt") as f: # cherche le mot dans le fichier en fonction d'"alea"
        for der in range(alea):
            motdevine=f.readline()
    #print(motdevine)
    for frt in range(len(motdevine)-1): # génere le mot en remplaçant les lettres par des tirets
        print("-",end="")
        reconstmot+="-"
    print()
    motdevine=motdevine.upper() # met en majuscule le mot du fichier
    print("le mot fait "+str(len(motdevine))+" caractères")

    while loose<7 and out==False: #tant que les erreurs sont inférieur à 7 et et out== False
        verif=reconstmot
        lettre=input("Quelle lettre ???").upper() # demande la lettre et la met en maajuscule
        lettredonné+=lettre #conserve les lettres données
        if lettre in reconstmot : # indique si la lettre à été déja donné (enlève une vie quend même (la vie est cruelle))
            print("La lettre "+lettre+" a déjà été donnée")

        for ertf in range(len(motdevine)-1): #remplace la lettre dans le mot avec des tirets
            if reconstmot[ertf]=="-":
                if lettre == motdevine[ertf]:
                    reconstmot=reconstmot[:ertf]+lettre+reconstmot[ertf+1:]

        if verif==reconstmot: #si le mot avec des tirets n'a pas changé avant la demande de lettre et après le remplacement des lettre --> enlève uun point
            loose+=1
            print("Il ne te reste plus que "+str((7-loose))+" vie")
            print(po.dessinPendu(loose-1))

        print(reconstmot) #affiche le mot avec des tirets
        print("Tu aas déjà donné les lettres suivantes : "+lettredonné) # affiche les lettres données

        if "-" not in reconstmot: # si le mot ne contient plus de tirets --> affiche félicitations
            print("Félicitation, tu viens de gagner avec seulement",loose,"erreurs")
            out=True #sort du jeu


        if loose>=7: # si le nombre d'erreur >=7 --> affiche que tu as perdu
            print("Tu as perdu, quel dommage car le mot était plutôt simple : c'était "+motdevine)
            out=True #sort du jeu

    print("Tableau des scores :") # affiche le tableau des scores limité à 10 (en fonction du nombre d'erreurs et du pseudo
    sco.actscore(7-loose,name)

    restart=input("appuie sur entrée pour recommencer (et faire mieux que ce minable résultat)")  #si restart =="" le jeu recommence

print("\nvous venez d'utiliser la version 3.1 du pendu développé par P. Bosseboeuf \n2021 version beta") # affiche informations légales





