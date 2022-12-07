liste = []
result = 0
for i in range(1000):
    a=i//100
    b=i//10
    b=b%10
    c=i%10
    abc = a+b+c
    print(abc)
    if abc==11:
        result+=1
    if i%7==0:
        result+=1
    if result==2:
        liste.append(i)
    result=0
print(liste)