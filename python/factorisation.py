y = int(input("donner le nombre a factoriser : "))
fact = 1
for i in range (1,y+1):
    fact = fact *i
print(y,"! = ",fact)