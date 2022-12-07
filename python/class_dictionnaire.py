# coding: utf-8
"""
Créer le samedi 15 Janvier 2022  
@auther: Mucka
"""
from cmath import pi
from itertools import count
from turtle import width

x = 0
liste_1 = []
liste_2 = []
for i in range(10):
    liste_1.append(i**2)
liste_2=[i**2 for i in range(10)]
if liste_1 == liste_2:
    print('c\'est les deux même')
else:
    print('les deux sont différentes')

liste_3 = [[i for i in range(3)] for j in range(3)]
print(liste_3)

#création d'un dictionnaire avec prénoms + clés
dictionnaire_1 = {
    '1':'Marie',
    '2':'Bernard',
    '3':'Didier',
    '4':'Angéline',
    '5':'Clémence',
    '6':'Paul'
}

#création d'un tableau de prénoms
prenoms = ['Marie','Bernard','Didier','Angéline','Clémence','Paul']

#créer une association entre les clés et les valeurs pour un tableau
dico_1 = {Key:Value for Key,Value in enumerate(prenoms)}
print("\ndictionnaire 1 tout :\n",dico_1,"\ndictionnaire 1 clés :\n",dico_1.keys(),"\ndictionnaire 1 valeurs :\n",dico_1.values())
sexe = ["F","M","M","F","F","M"]
dico_2 = {prenoms:sexe for prenoms,sexe in zip(prenoms,sexe)}
print("\ndictionnaire 2 tout :\n",dico_2,"\ndictionnaire 2 clés :\n",dico_2.keys(),"\ndictionnaire 2 valeurs :\n",dico_2.values(),'\n')
dico_3 = {prenoms:sexe for prenoms,sexe in zip(prenoms,sexe)if sexe=='F'}
dico_4 = {prenoms:sexe for prenoms,sexe in zip(prenoms,sexe)if sexe=='M'}
print('liste des Femmes',dico_3.keys())
print('liste des Hommes',dico_4.keys())

tuples_1 = tuple(i**2 for i in range(10))
print(tuples_1)

round_pi = round(pi*2)+pi
liste_4 = [True,True,False,True]
print(all(liste_4),round_pi/3)
print('\n',type(liste_1),'\n',type(dico_1),'\n',type(tuples_1),'\n',type(x))

#format idéal pour les réseaux neuronaux 
y = int(input('entrez un nombre : '))
print('\nle nombre :',y,'\nen binaire :',bin(y),'\nen octet :',oct(y),'\nen hexa :',hex(y))

format_VILLE = str(input('entrez une ville : '))
format_TEMP = int(input('entrez la température : '))
message = "la température est de {} °C à {}".format(format_TEMP,format_VILLE)
print(message)

f=open('open.html','w')
f.write('<!DOCTYPE html><html><head>\n\n<title>Title of the document</title></head><body>\n\n<p>Un formulaire avec differents types de champs</p>\n\n<form action="getform.php" method="get">\n\n\n\n<label>Prenom : <input type="text"></label><br>\n\n\n\n<label>Nom : <input type="text"></label><br>\n\n\n\n<label>Adresse email : <input type="email"></label><br>\n\n\n\n<input type="submit" value="Envoyer">\n\n</form>\n\n<form>\n\n\n\n<label for="name">Saisir un nom d\'utilisateur <i>lettres minuscules et majuscules :</i> </label>\n\n\n\n<input type="text" name="name" id="name" required pattern="[A-Za-z]+">\n\n\n\n<button>Envoyer</button>\n\n</form></body></html>')

with open('open.py','w') as f:
    exp = int(input('entrez la valeur de l\'exposant :'))
    for i in range(10):
        f.write('{} exp {} = {}\n'.format(i,exp,i**exp))