"""
À chaque coup d'épée, Hercule coupait la moitié des têtes restantes.
Si après une coupe, il restait un nombre impair de têtes, alors le nombre de têtes restantes triplait instantanément, et une tête supplémentaire repoussait encore.
Si à un moment l'Hydre ne possédait plus qu'une seule tête, Hercule pouvait l'achever d'un coup d'épée supplémentaire.

Si l'Hydre a 6 têtes, Hercule en coupe la moitié au premier coup d'épée. Il en reste 3. 
            Instantanément, le nombre de têtes triple et il en pousse une autre. Il y a maintenant 10 têtes.
Au second coup d'épée, Hercule en coupe 5. Des têtes repoussent, il y en a maintenant 16.
Au 3e coup d'épée, Hercule coupe 8 têtes. Il en reste 8. Rien ne repousse.
Au 4e coup d'épée, Hercule coupe 4 têtes, il en reste 4. Rien ne repousse.
Au 5e coup d'épée, Hercule coupe 2 têtes, il en reste 2. Rien ne repousse.
Au 6e coup d'épée, Hercule coupe une tête. Il n'en reste plus qu'une.
Le 7e et dernier coup d'épée permet d'achever l'Hydre.

Si l'Hydre a 6 têtes, Hercule doit donc donner 7 coups d'épée pour la vaincre.
8188
"""
nbtete = 8188
coup=0
while nbtete != 1:
    print(nbtete)
    coup+=1
    nbtete=nbtete/2
    if nbtete%2!=0:
        nbtete=nbtete*3+1
    if nbtete==2:
        nbtete=1
print(coup+2)

"""
# Définissez le nombre de têtes initial de l'Hydre
num_heads = 8188

# Initialisez le compteur de coups d'épée à 0
num_swords = 0

# Répétez jusqu'à ce qu'il ne reste qu'une seule tête
while num_heads > 1:
    # Coupez la moitié des têtes restantes
    num_heads = num_heads // 2
    
    # Si le nombre de têtes est impair, le nombre de têtes triplera
    # instantanément et une tête supplémentaire repoussera
    if num_heads % 2 != 0:
        num_heads = num_heads * 3 + 1
    
    # Incrémentez le compteur de coups d'épée
    num_swords += 1

# Donnez un dernier coup d'épée pour achever l'Hydre
num_swords += 1

# Affichez le nombre total de coups d'épée nécessaires
print(num_swords)
"""