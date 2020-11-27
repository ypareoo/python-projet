# Créé par Admin, le 27/10/2020 en Python 3.7
# bibliothèque des fonctions pour le tp du même nom
from turtle import*

def branche (LONGUEUR,cotcarré):
    """trace une branche en fonction :
        1-de la longueur de la branche
        2-de la longueur du côté du carré"""
    forward(LONGUEUR)
    for t in range (4):
        right(90)
        forward(cotcarré)
    backward(100)

def carré (coté):
    """trace un carré en fonction de la longueur de son côté"""
    for tu in range(4):
        forward(10)
        left(90)

def étoile (branche,taille,remplissage=None):
    """trace une étoile en fonction de la longueur du segment-type principal
    et optionnellement de son remplissage"""
    if remplissage!=None:
        color(remplissage)
        begin_fill()
    if branche==5:
        for hgu in range(branche):
            forward(taille)
            right(144)
    if remplissage!=None:
        end_fill()


def rectangle_coordonnée (abssupgau,ordonnéesupgau,absinfdroi,ordinfdroit,remplissage=None):
    """trace un rectangle à partir du coin inférieur gauche en fonction des coordonnées du coin supérieur gauche
    et du coin inérieur droit
    et optionnellement de son remplissage"""
    if remplissage!=None:
        color(remplissage)
        begin_fill()
    goto(abssupgau,ordonnéesupgau)
    goto(absinfdroi,ordonnéesupgau)
    goto(absinfdroi,ordinfdroit)
    goto(abssupgau,ordinfdroit)
    if remplissage!=None:
        end_fill()

# by P. Bosseboeuf industry; department 1G7