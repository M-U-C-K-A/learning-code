n = 100
while True:
    try:
        x = int(input('nombre de jour : '))
        break
    except ValueError:
        print('Oops! une erreur est apparue, veuillez réessayer...')

for i in range(x+1):
    print(i,' => ',round(n,2),'% d\'améliorations par rapport au jour 1')
    n=n*1.01