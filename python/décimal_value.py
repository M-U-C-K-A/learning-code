
list = []
for i in range(1,396):
    k = i
    kc = k//100
    kd = (k//10)%10
    ku = (k%100)%10
    if kc !=4:
        if kd !=4:
            if ku !=4:
                list.append(1/i)
e = sum(list)#resultat
print(e)

"""
DECOMPOSITION CENTAINE EN STRING : 100 = "1","0","0"
i = 426
i = i//100

i = 426
i = (i//10)%10

i = 426
i = (i%100)%10
"""