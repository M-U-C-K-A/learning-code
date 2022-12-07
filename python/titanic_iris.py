# coding: utf-8
"""
Créer le lundi 21 Février 2022  
@auther: Mucka
"""
#19/30 Visualisation de Données avec Seaborn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())
#1. Pairplot() : La vue d'ensemble
sns.pairplot(iris, hue='species')
#2. Visualiser de catégories
titanic = sns.load_dataset('titanic')
titanic.drop(['alone', 'alive', 'who', 'adult_male', 'embark_town', 'class'], axis=1, inplace=True)
titanic.dropna(axis=0, inplace=True)
print(titanic.head())
sns.catplot(x='survived', y='age', data=titanic, hue='sex')
plt.figure(figsize=(32, 8))
sns.boxplot(x='age', y='fare', data=titanic, hue='sex')
#3. Visualisation de Distributions
sns.displot(titanic['fare'])
sns.jointplot('age', 'fare', data=titanic, kind='hex')
sns.heatmap(titanic.corr())

"""
Ce code utilise la bibliothèque de visualisation de données Seaborn pour visualiser des données de deux jeux de données : 
"iris" et "titanic". Dans la première partie du code, un "pairplot" est créé pour afficher les différentes variables du jeu de données "iris". 
Dans la deuxième partie, des visualisations de catégories sont créées pour le jeu de données "titanic", y compris une visualisation "catplot" et un boxplot. 
Enfin, dans la dernière partie, des visualisations de distributions sont créées pour le jeu de données "titanic", y compris un "displot" et un "jointplot". 
Une "heatmap" est également créée pour afficher les corrélations entre les différentes variables du jeu de données "titanic".
"""