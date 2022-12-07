# coding: utf-8
"""
Créer le Mercredi 19 Janvier 2022  
@auther: Mucka
"""
import statistics
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
A = np.random.randint(0,10,[2,3])
B = np.ones((2,1))
C = A+B
print('this is A :\n{}\n this is B : \n{}'.format(A,B))
print('Voici A+B :\n{}'.format(C))
print()
D = np.random.randint(0,10,[4,1])
E = np.random.randint(0,5,[1,6])
E = E*2
F = D+E
print('this is D :\n{}\n this is E : \n{}'.format(D,E))
print('Voici D+E :\n{}'.format(F))
org_array = np.array([[23, 46, 85], 
                      [43, 56, 99], 
                      [11, 34, 55]]) 
print(org_array) 
heit = np.array([ 1 , 2 , 3 , 4 ])
asw32 = np.array ([ 1 , 2 , 3 , 4 ], dtype = np.float32)
fig = plt.figure(figsize=(12,8))
fig.patch.set_facecolor('black')
ax = plt.axes()
ax.set_facecolor('black')


x = np.linspace(0,2,10)
y = x**2
print(x)
plt.show()

def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values
text = input("Enter a string: ")
s1=0
s2=0
print(to_ascii(text)) #optionnel
for k in range(len(text)):
    print(text[k]) #optionnel
    c = to_ascii(text[k])
    c = c[0]
    print(c)
    s1 = s1 + c
    s2 = s2+(c*(k+1))
s1 = s1%256
s2 = s2%256
s1 = hex(s1)
s2 = hex(s2)
print("Valeur de '{}' après son hash : '{} {}' ".format(text,s1,s2))