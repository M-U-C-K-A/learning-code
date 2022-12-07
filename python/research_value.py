u = 9697
n = 105
for i in range(106):
    u1 = u//100
    u2 = u%100
    u3 = u1+u2
    u3=(u3*188+188)%9973
    u=u3
print(u)
