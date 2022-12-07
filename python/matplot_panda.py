# coding: utf-8
"""
Créer le lundi 24 Janvier 2022  
@auther: Mucka
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('titanic3.xls')
print(data.shape)
print(data.head)
data = data.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'],axis=1)
print(data.head)
data.describe()
data = data.dropna(axis=0)
data.shape
data.describe()
data['pclass'].value_counts().plot.bar()
data['age'].hist()
print(data.groupby(['sex','pclass']).mean())
data['age']