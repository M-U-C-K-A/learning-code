V = 0
E = 0
A = 0
liste = []
import matplotlib.pyplot as plt
for i in range(100):
    E =3-0.005*V
    A += E
    V = 8*E
    print(E,A,'   ',i)
    liste.append(E)
plt.plot(liste)
plt.show()