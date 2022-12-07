bleu = 2
rouge = 0
vert = 0
total = 0
for i in range(34):
    rouge = 7*bleu
    vert = 5*bleu
    bleu = (rouge+vert)%100
    print(rouge+vert,'  ',bleu)
    total += bleu+rouge+vert
print(total+2)