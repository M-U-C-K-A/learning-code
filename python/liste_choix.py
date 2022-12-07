from re import A


liste = (47, 13, 19, 62, 84, 32, 50, 42, 91, 93, 34, 19, 92, 35, 19, 4, 17)
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in range(len(liste)):
    w = liste[i]
    for j in range(3):
        if w-50>=0:
            w+=-50
            a+=1
    for j in range(3):
        if w-20>=0:
            w+=-20
            b+=1
    for j in range(3):
        if w-10>=0:
            w+=-10
            c+=1
    for j in range(3):
        if w-5>=0:
            w+=-5
            d+=1
    for j in range(3):
        if w-2>=0:
            w+=-2
            e+=1
    for j in range(3):
        if w-1>=0:
            w+=-1
            f+=1
print(a,b,c,d,e,f)