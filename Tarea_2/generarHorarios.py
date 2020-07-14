import random

def generarHorarios():
    n = random.randint(3, 10)
    print(str(n))
    
    for i in range(n):
        inicio = random.randint(1, 18)
        fin = random.randint(inicio+1, 19)
        print(str(inicio),end='')
        print(" ",end='')
        print(str(fin),end='')
        print("\n",end='')
            
generarHorarios()