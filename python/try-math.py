from math import *
from random import *
from time import *
from os import system
loading =("■▢▢▢▢▢▢▢▢▢ 10% ","■■▢▢▢▢▢▢▢▢ 20% ","■■■▢▢▢▢▢▢▢ 30% ","■■■■▢▢▢▢▢▢ 40% ","■■■■■▢▢▢▢▢ 50% ","■■■■■■▢▢▢▢ 60% ","■■■■■■■▢▢▢ 70% ","■■■■■■■■▢▢ 80% ","■■■■■■■■■▢ 90% ","■■■■■■■■■■ 100%")

def load(loading):
    for i in range(10):
        print(loading[i])
        sleep(.02)
        system("cls")


while True:
    try:
        rayon = int(input('rayon du cercle : '))
        break
    except ValueError:
        print('Oops! une erreur est arrivé. Try again...')

system("cls")
print('parfait !')
load(loading)
system("cls")

diametre = 2*rayon
perimetre = diametre*2
aire =(2*rayon)*pi

print('○')
print(f"Pour un cercle de rayon {rayon}:")
print(f"le diametre est de {round(diametre,2)}")
print(f"le périmetre est de {round(perimetre,2)}")
print(f"l'aire est de {round(aire,2)}")

print('---------------')

volume = (4*pi*pow(rayon,3)/3)
aire = 4*pi*pow(rayon,2)
rapport_aire_volume = aire/volume
Ricci_scalaire = 2/pow(rayon,2)

print('◉')
print(f"Pour une sphere de rayon {rayon}:")
print(f"le volume est de {round(volume,2)}")
print(f"l'aire est de {round(aire,2)}")
print(f"Sa « compacité » rapport aire-volume est de {round(rapport_aire_volume,2)}")
print(f"son scalaire de Ricci est de {round(Ricci_scalaire,2)}")

print('---------------')

print('◍')
print(f"Pour une N-sphere de rayon {rayon}:")
sum_impair = 1
for n in range(1,9):
    #calcul de la fonction gamma
    if n%2==0:
        gamma=pow(pi,n/2)*pow(rayon,n)/factorial(n/2)
    else:
        gamma=pow(2,(n+1)/2)*((pow(pi,(n-1)/2)*pow(rayon,n))/sum_impair)
        sum_impair=sum_impair+2

    volume=(pow(pi,n/2)*pow(rayon,n))/gamma*(n/2+1)
    print(f"volume {volume,n}")