x =797114
u = x//1000
n = x%1000
for j in range(n):
    u=u*13
    u = u%1000
    print(u)