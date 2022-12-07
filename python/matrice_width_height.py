# coding: utf-8
"""
Créer le dimanche 16 Janvier 2022  
@auther: Mucka
"""
import math
import random
from xml.etree.ElementTree import PI
import numpy as np
for i in range(5):
    B_zeros = np.zeros((3*i,3*i))
    B_Array = np.array([i,2*i,2**i])
print("that was b whith 0 : \n{}\n and that was whith number : \n{}".format(B_zeros,B_Array))    
i = 0
for i in range(12):
    A = np.array(['divided by 2 👉',i/2,'multipled by 2 👉',i*2,'increase by 2 👉',i+2])
    print(A)

C = np.ones((4,5))
print(C)
E = np.zeros((4,5))
print(E)

np.random.seed(0)
D = np.random.randn(2,4,3)
print(D)

print(np.eye(4,3))
print(np.linspace(0,10,13))
print(np.arange(0,10,1))
print("\nvertical : \n",np.vstack((E,C)),"\n\nhorizontal : \n",np.hstack((E,C)))
print("Taille de D :",D.size,"\nTaille de E :",E.size)
F_old = np.array([1,2,3])
F_new = F_old.reshape((F_old.shape[0],1))
print("that was the old : {} and that was the new : {}".format(F_old.shape,F_new.shape))

