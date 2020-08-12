import fileinput

def crearMatriz(camino1,camino2):#creacion de la matriz
    filas = []
    for fil in range(len(camino1)):
        columnas = []
        for col in range(len(camino2)):
            columnas.append("")
        filas.append(columnas)
    # print(len(camino1),len(camino2))
    # print(filas)
    return filas

def sub_mas_larga(camino1,camino2): #algoritmo de PD subsecuencia más larga
    matriz = crearMatriz(camino1,camino2)
    for i in range(len(camino1)):
        for j in range(len(camino2)):
            if (camino1[i] == camino2[j]):
                if (i == 0 or j == 0):
                    matriz[i][j] = camino1[i]
                else:
                    matriz[i][j] = matriz[i-1][j-1] + camino1[i]
            else:
                matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1], key=len) #se agrega el maximo en base al largo

    subsecuencia = matriz[-1][-1]

    return subsecuencia

t = int(input())
numbers = list(map(int, list(input().rstrip().split(" ")))) 
caminos = []
for camino in fileinput.input():
    caminos.append(camino.rstrip())
    
for i in range(t):
    final = sub_mas_larga(caminos[0], caminos[1])
    for i in range(len(final)):
        print(final[i], end="")
    print("")
        