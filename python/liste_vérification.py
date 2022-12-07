liste = [12, 24, 31, 77, 87, 103, 112, 145, 181, 197, 205, 217, 224, 225, 228, 255, 263, 278, 289, 297]
for i in range(len(liste)):
    for j in range(len(liste)):
        if liste[i]+liste[j] == 1881:
            print(liste[i],liste[j])
        else:
            print(liste[i],liste[j])