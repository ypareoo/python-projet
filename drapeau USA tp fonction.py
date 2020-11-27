# Créé par BOSSEBP, le 28/09/2020 en Python 3.4
# Créé par Admin, le 27/09/2020 en Python 3.7
#drapeau USA

"""FONCTIONS
######################"""

from turtle import*
from géometrie import*

"""PROGRAMME PRINCIPALE
##############################"""

title("Drapeau USA")   #nomme la fenêtre de dessin
delay(0) #délai en miliseconde entre deux rafraichissement
speed(999)  #aller vite
#----------------------------
down()
rectangle_coordonnée(0,100,190,0,"red") #trace rectangle
up()

#---------------------------
color("white")   #bandes blaches
width(7.2)
ord=3
a=3.846
goto(0,ord*a)
down()
forward(190)
up()
ord=7
for x in range (0,5,1):
    goto(0,ord*a)
    down()
    forward(190)
    up()
    ord=ord+4

#---------------------------
goto(0,46) #trace rectangle bleu
width(1)
down()
rectangle_coordonnée(0,100,75,46,"blue")
up()

"""-----------------------------
PARITE LA PLUS INTÉRESANTE DU PROGRAMME :
----------------------------le traçage des étoiles"""

width(0.01)
back=1.5 #définie la taille de l'étoile
av=back*2 #la longueur utilisée pour le traçage de l'étoile utilise la variable back pour pouvoir changer rapidement de valeur au besoin

g=0
h=0
j=0
for r in range (0,2,1):   #série X2

    for k in range (0,6+g,1): #répète vers la droite l'étoile
        f=0+j
        for z in range(0,5+g,1):   #répète vers le bas l'étoile

            goto(6.3+6.3*h,94.6-5.4*f)
            down()
            begin_fill()
            backward(back)
            étoile(5,av,"white")
            end_fill()
            up()
            f=f+2   #ordonnée
        h=h+2  #abscisse
    g=g-1  #la deuxième série possède une ligne et colonne en moins
    h=1    #augmente/décale les abscisses pour la deuxième série
    j=j+1  #diminue/décale les ordonnée pour la deuxième série


ht()

goto(0,-70)
color("black")
write("Et voila un drapeau dont donald peut être fier !",move=False, align='center', font=('Arial', 18, 'normal'))

exitonclick()

# by P. Bosseboeuf industry; department 1G7
