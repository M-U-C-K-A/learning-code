a,b,c,e,c,g,f,m,o,h,p,s,v = 1,2,3,4,5,6,7,8,9,10,11,12,13
liste = [a,b,c,e,c,g,f,m,o,h,p,s,v]
i=5
k = 0
j=0
print(liste)
while i!=0:
    k+=1
    liste[i],liste[i-1]=liste[i-1],liste[i] 
    for k in range(4):
        if liste[k]==a:
            j+=1
        if liste[k]==e:
            j+=1
        if liste[k]==g:
            j+=1
        if liste[k]==h:
            j+=1
    
    i=i+5
    if i>=13:
        i=i-13
    if j==4:
        i=0
    else:
        j=0
print(k)
print(liste)