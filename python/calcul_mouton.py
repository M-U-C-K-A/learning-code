bleu = 2
rouge = 0
vert = 0
total = 0
for i in range(34):
    rouge = 7*bleu
    vert = 5*bleu
    bleu = (rouge+vert)%100
    print(rouge+vert,'  ',bleu)
    total += bleu+rouge+vert
print(total+2)
#Ce code permet de calculer le nombre total de bleus, rouges et verts dans une série de 34 itérations. 
#La boucle for parcourt les 34 itérations, en utilisant les valeurs des couleurs précédentes pour calculer le nombre de bleus, rouges et verts pour chaque itération. 
#Le nombre total de chaque couleur est ensuite ajouté au total global, puis le résultat final est affiché en ajoutant les 2 bleus initiaux.
