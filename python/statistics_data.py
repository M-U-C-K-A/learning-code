# coding: utf-8
"""
Créer le dimanche 16 Janvier 2022  
@auther: Mucka
"""
from curses.textpad import rectangle
import math
import random
import statistics
import os
import glob
from turtle import width
liste = [51,15,65,324,984,54,84,3574,43,1,3,1,3186,135,23,2,1,45,4,9]
print('liste :',liste)
for x in range(4):
    random.shuffle(liste)
    print('liste mélangé {} :'.format(x+1),liste)
print('mediane :',round(statistics.median(liste)))
print('moyenne :',round(statistics.mean(liste)))
print('variance :',round(statistics.variance(liste)))
print('Pvariance :',round(statistics.pvariance(liste)))

print('0 débat le plus beau c\'est clairement :',random.choice(['Alexy','Hugo','Evan']))
print('au fait, voici son num : +33',random.randint(1,9),random.randint(10,99),random.randint(10,99),random.randint(10,99),random.randint(10,99),random.randint(10,99))
random.seed(115)


