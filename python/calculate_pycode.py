#importation des librairies
from math import *
from random import *
#définition des variables
A,B,C=3,4,2
width, height, depth = 160, 44, 20
#création des fonctions de calculs
def calculateX(i, j, k):
    return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) + j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C)

def calculateY(i, j, k):
    return j * cos(A) * cos(C) + k * sin(A) * cos(C) - j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) * i * cos(B) * sin(C)

def calculateZ(i, j, k):
    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B)

square = [[],[],[],[],[],[],[],[]]
def main(w, q, d):
    for i in range(1,9):
        w = width//i
        q = height//i
        d = depth//i
        w=calculateX(w,q,d)
        q=calculateY(w,q,d)
        d=calculateZ(w,q,d)
        square[i-1].append(round(w,2))
        square[i-1].append(round(q,2))
        square[i-1].append(round(d,2))
    return square
print(main(8,12,51))