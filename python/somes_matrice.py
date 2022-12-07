# coding: utf-8
"""
Créer le Lundi 17 Janvier 2022  
@auther: Mucka
"""
import math
import random
from xml.etree.ElementTree import PI
import numpy as np

Anb = [1,1]
print(Anb)
print()
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)

print('\nla première colonne : {}\nla première ligne : {}'.format(A[:,0],A[0,:]))

print('\n avec la premiere méthode :(précisant le numéro)')
for i in range(3):
    print(A[i,:], 'ligne : {}'.format(i+1))

print('\n avec la deuxieme méthode :(précisant l\'axe)')
for i in range(3):
    print(A[i], 'ligne : {}'.format(i+1))

print('\n avec la troisieme méthode :(précisant la ligne)')
for i in range(3):
    if i==2:
        print(A[0:i+1,0:i+1], 'voici le tableau')
print()
print(A[:,-2:])

#changer le carrée du millieux
B=np.zeros((4,4))
B[1:3,1:3]=1
print('\n',B)

#intégrer le pas (une sur deux, une colonne sur deux)
C=np.zeros((5,5))
C[::2,::2]=1
print('\n',C)

# changement avec de l'aléa
D = np.random.randint(1,10,[5,5])
print('\n',D)
D[D<=5]=random.randint(6,10)
print('\n',D)
D[(D<=7)!=(D==8)]=random.randint(1,10)
print('\n',D)

"""
def initialisation(m,n):
    X=np.random.randn(m,n)
    X=np.concatenate((X,np.ones((X.shape[0],1))),axis=1)
    return X
print(initialisation(3,2))
"""