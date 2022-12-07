from time import *
def decompte():
  n = 10
  while n:
    print(n)
    n -= 1
    sleep(0.2)
  print("Décollage !")
decompte()