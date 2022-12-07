# coding: utf-8
"""
Créer le dimanche 23 Janvier 2022  
@auther: Mucka
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0,10,20)
y = x**2
plt.subplot(3, 2, 1)
plt.scatter(x,y)
f = interp1d(x,y,kind='linear')
plt.title('linear')
new_x = np.linspace(0,10,50)
result = f(new_x)
plt.subplot(3, 2, 2)
plt.scatter(x,y)
plt.scatter(new_x,result,c='r',s=3)


x = np.linspace(0,10,10)
y = np.sin(x)
plt.subplot(3,2,5)
plt.scatter(x,y)
f = interp1d(x,y,kind='cubic')
plt.title('cubic')
new_x = np.linspace(0,10,50)
result = f(new_x)
plt.subplot(3, 2, 6)
plt.scatter(x,y)
plt.scatter(new_x,result,c='r',s=3)
plt.show()