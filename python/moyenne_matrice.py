# coding: utf-8
"""
Créer le Mardi 18 Janvier 2022  
@auther: Mucka
"""
import statistics
import numpy as np
np.random.seed(0)
A = np.random.randint(0,10,[3,4])
print('la matrice : \n{}'.format(A))
print('leur emplacement vertical dans la matrice : {}'.format(A.argmin(axis=0)+1))
print('leurs valeurs dans la matrice : {}'.format(A.min(axis=0)))
#print('les valeurs réaranger : {}'.format(A.argsort()))
print(np.corrcoef(A)[0,1],'\n')
#test des apparitions de chaque nombre

B = np.random.randint(0,100,[10,5])
print(B)
for i in range(10):
    C = np.random.randint(0,(i*20)+1,[10,5])
    D = B+C
    if i ==9:
        if D.all()==(B.all()+C.all()):
            print("voici le tableau D : \n{}".format(D))
        else:
            X_prima = (B-B.mean(axis=0))/B.std(axis=0)
            print("voici la moyenne standardisé par l'axe 0 :\n{}".format(X_prima))
    else:
        print("pas encore : {}".format(i+1))