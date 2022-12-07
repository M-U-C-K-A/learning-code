a=0
b=1
c=0
e=0
liste = []
for i in range(70):
    c=a+b
    a=b
    b=c
    d = str(c)
    for j in range(len(d)):
        e +=int(d[j])
    print(e)
"""
Ce programme génère la suite de Fibonacci et affiche la somme des chiffres de chaque élément de la suite. 
La suite de Fibonacci est une suite de nombres où chaque nombre est la somme des deux nombres précédents dans la suite. 
Par exemple, la suite de Fibonacci commence comme suit : 1, 1, 2, 3, 5, 8, 13, etc.

Le code initialise les variables a, b, et c à 0, 1 et 0 respectivement. La variable a représente le premier nombre dans la suite de Fibonacci, 
la variable b représente le deuxième nombre dans la suite, et la variable c est utilisée pour stocker la somme des deux nombres précédents à chaque itération de la boucle.

La boucle for parcourt la suite de 70 éléments, 
en calculant la somme des variables a et b à chaque itération pour obtenir le nombre suivant dans la suite, 
en stockant le résultat dans la variable c. 
Ensuite, le code convertit le nombre en chaîne de caractères pour pouvoir parcourir chaque chiffre individuellement et calculer la somme de ces chiffres. 
Enfin, la somme des chiffres est affichée.
"""