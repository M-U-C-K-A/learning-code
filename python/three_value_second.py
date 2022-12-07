from matplotlib.transforms import Bbox

a,b,c,k,n = 1,4,3,1,0
while k<1000-n:
    a = b 
    b = c+a
    c = -4*c-3*a-b
    n = a+b 
    k+=1
print(a,b,c)
"""
Ce code utilise une boucle pour calculer les valeurs suivantes de a, b, et c en utilisant une série de formules. 
À la fin de la boucle, les dernières valeurs calculées pour a, b, et c sont imprimées. 
Cependant, étant donné que la boucle ne fait que continuer à itérer jusqu'à ce qu'un certain nombre de conditions soient remplies, 
il n'est pas clair ce que ces valeurs représentent ou à quoi elles peuvent servir.
"""