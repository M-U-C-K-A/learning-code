import math
n = 13979
rac_n = math.sqrt(n)
for i in range(n):
    for j in range(n):
        if (i**2)+(j**2)==(n**2):
            print(i,',',j)
            print(i**2,'    ',j**2)