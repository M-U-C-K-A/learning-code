# coding: utf-8
"""
Créer le vendredi 14 Janvier 2022  
@auther: Mucka
"""
from cmath import pi


villes = ['Paris','Berlin','Londres','Bruxelles']

villes.append('Dublin')
print(villes)

villes.insert(3,'Dunkerque')
print(villes)

villes_2 =['Caen','Elbeuf']
villes.extend(villes_2)
print(villes)

art = len(villes)
print(art*pi/3)

villes.remove('Caen')
print(villes)

villes.sort
print(villes)
villes.sort(reverse=True)
print(villes)

ville= ['aaa','ccc','bbb','ddd','eee','fff']
print(ville)
ville.sort()
print(ville)
ville.sort(reverse=True)
print(ville)



i='aab'
if i in ville:
  print(i,'se situe bien dans la liste')
else:
  print(i,'ne se situe pas dans ville')

for index,valeur in enumerate(ville):
  print(index,valeur)

for a,b in zip(ville,villes):
  print(a,b)

a=1
test = []
while a<=10:
  test.append(a)
  test.append('🐍')
  a+=1
  print('⚠️ temporaire ⚠️',test,'⚠️ temporaire ⚠️')


print('✅',test)

#fibonacci
def fibonacci(n):
  a=0
  b=1
  while a<=n:
    print('✦',a,'✦')
    a,b=b,a+b
fibonacci(21)


from cmath import pi
import time
start = time.time()
lit = [i**2 for i in range(3)]
print(lit)
def liste_step_Two():
    comp = [[i for i in range(y*2)] for y in range(5)]
    comp.remove([])
    comp.insert(0,[0]) 
    print(comp,'🍃')
liste_step_Two()
emoji = ['🌿','☘️','🍀','🎋','🌼','🍃','🍂','🍁','🍄','🐚','🌹','🥀','🌺','🌸','🌵','🎄','🌲','🌳','🌴','🌱']
types = ['05','02','03','12','15','07','08','09','02','04','06','05','54','10','12','25','38','45','20','01']
tape = {}
print('nb de types :',len(emoji))
print('nb de longueur :',len(types))
for index,emoji in enumerate(emoji, 0):
  tape[types[index]] = emoji
print(tape)

end = time.time()
print(end-start)