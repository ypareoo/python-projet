import random as ra
from pathlib import*
from turtle import*


def actscore(score,pseudo):

    out=False
    listevar=["a","b","c","d","e","f","g","h","i",'j']
    liste=[1,2,3,4,5,6,7,8,9,10]
    #print(score)
    with open ("score.txt","r") as sco:
        for i in range(10):
            liste[i]=int(sco.readline()[:1])

    with open ("score.txt","r") as sco:
        for i in range(10):
            listevar[i]=sco.readline()



    with open ("score.txt","r") as sco:
        for z in range(10):
            if score>=liste[z] and out==False:
                listevar.insert(z,str(score)+pseudo)
                out=True

    for i in range(len(listevar)):
        if listevar[i][-1]=="\n":
            listevar[i]=listevar[i][:-1]

    with open ("score.txt","w") as sco:
        for y in range(10):
            sco.write(str(listevar[y])+"\n")

    with open ("score.txt","r") as sco:
        for i in range(len("score.txt")):
            print(sco.readline(),end="")
    return







