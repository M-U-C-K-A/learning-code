
nterms = int(input("Entrez un nombre: "))
 
n1 = 0
n2 = 1
 
print("\n la suite fibonacci est :")
print(n1, ",", n2, end=", ")
 
for i in range(2, nterms):
  suivant = n1 + n2
  print(suivant, end=", ")
 
  n1 = n2
  n2 = suivant
  """
   la suite fibonacci est :
0 , 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 
1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 
514229, 832040, 1346269, 2178309, 3524578, 5702887, 
9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 
165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 
2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 
53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 
956722026041, 1548008755920,
 2504730781961, 4052739537881, 6557470
 
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