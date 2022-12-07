import random
data = []
x = int(input("nombre de lignes : "))
y = int(input("nombre de colones : "))
def new_func(data, x):
    if x==1:
        data.append('█')
    elif x==2:
        data.append('▄')
    elif x==3:
        data.append('▀')
    elif x==4:
        data.append('▓')
    elif x==5:
        data.append('▒')
    elif x==6:
        data.append('░')

for i in range(y*x+1):
    x= random.randint(1,6)
    new_func(data, x)

for j in range(y):
    print(j+1,end='')
print('')
e = 0
for i in range(1,len(data)):
    print(data[i],end='')
    if i%y==0:
        print(f' {e+1}')
        e+=1