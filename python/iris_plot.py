# coding: utf-8
"""
Créer le Jeudi 20 Janvier 2022  
@auther: Mucka
"""
import statistics
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import projections
iris = load_iris()
x = iris.data
y = iris.target
names = list(iris.target_names)
"""
print({x.shape[0]},{x.shape[1]})
print({np.unique(y).size})
plt.show()
"""
ax = plt.axes(projections='3d')
ax.scatter(x[:,0],x[:,1],x[:,2])
plt.show()