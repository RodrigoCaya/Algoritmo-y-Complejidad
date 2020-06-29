import random

def generarMatrices():
    n = 2 ** random.randint(0, 4)
    
    k = random.randint(1, 5)
    print(str(n) + " " + str(k))
    
    for i in range(n * k):
        for j in range(n):
            numero = random.randint(0, 30)
            print(str(numero),end='')
            print(" ",end='')
        print("\n",end='')

    for i in range(n):
        for j in range(n * k):
            numero = random.randint(0, 30)
            print(str(numero),end='')
            print(" ",end='')
        print("\n",end='')
            
generarMatrices()