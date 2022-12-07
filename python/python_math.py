from random import *
from statistics import *
from os import system

somme = []
a=1
b=6
nombre_de_dé = int(input('nombre de dé a lancer : '))
for _ in range(nombre_de_dé):
    dé = randint(a,b)
    somme.append(dé)
system("cls")
print('voici les dé', somme)
print(sum(somme))
print("score moyen des dé :",round(mean(somme),2))
print("la moyenne théorique est de :",(a+b)/2)
print("score médian :",round(median(somme)))
print("mode des dé :",round(mode(somme)))
print("stdev :",round(stdev(somme)))
print("la variance :",round(variance(somme)))