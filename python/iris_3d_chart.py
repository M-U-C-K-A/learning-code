# coding: utf-8
"""
Créer le dimanche 23 Janvier 2022  
@auther: Mucka
"""
from cmath import pi
import statistics
from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
iris = load_iris()
x = iris.data
y = iris.target
names = list(iris.target_names)
print(f'x contient {x.shape[0]} exemples et {x.shape[1]} variables')
print(f'il y a {np.unique(y).size} classes')

print({x.shape[0]},{x.shape[1]})
print({np.unique(y).size})
plt.show()

f = lambda x,y:np.sin(x)+np.sin(y)
X = np.linspace(0,5,100)
Y = np.linspace(0,5,100)
X,Y = np.meshgrid(X,Y)
Z = f(X,Y)
print(Z.shape)
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z,cmap='plasma')#couleur viridis plasma inferno magma cividis
plt.show() 

plt.hist(x[:,0],bins=20)
plt.hist(x[:,1],bins=20)
plt.show() 

plt.hist2d(x[:,0],x[:,1],cmap='Blues')
plt.xlabel("longueur sépal")
plt.ylabel("largeur sépal")
plt.colorbar()
plt.show() 
f = lambda x,y:np.sin(x)+np.sin(y)*np.cos(x)
q = lambda x,y:np.cos(x)+np.sin(x)*np.sin(y)

X = np.linspace(0,5,100)
Y = np.linspace(0,5,100)
X,Y = np.meshgrid(X,Y)
Z = f(X,Y)
W = q(X,Y)

plt.subplot(2, 1, 1)
plt.contourf(X,Y,Z,20,cmap='viridis')
plt.colorbar()
plt.subplot(2, 1, 2)
plt.contourf(X,Y,W,20,cmap='plasma')
plt.colorbar()
plt.show() 

from scipy import misc 
face = misc.face(gray=True)
#plt.subplot(2, 1, 1)
#plt.imshow(face,cmap='gray')
#plt.subplot(2, 1, 2)
#plt.hist(face.ravel(),bins=255)
#plt.show()

plt.imshow(np.corrcoef(x.T),cmap='Blues')
plt.xlabel("longueur sépal")
plt.ylabel("largeur sépal")
plt.colorbar()
plt.show()
