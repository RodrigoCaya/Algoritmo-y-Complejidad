linea_1 = input().rstrip().split(" ")
n = int(linea_1[0])
k = int(linea_1[1])

matriz_1 = []
matriz_2 = []

#guardamos valores primera matriz
for i in range(k * n):
    fila = list(map(int, input().rstrip().split(" ")))
    matriz_1.append(fila)

for i in range(n):
    fila = list(map(int, input().rstrip().split(" ")))
    matriz_2.append(fila)
   
def sum_matrices(matriz_1, matriz_2): #parametros: dos matrices y retorna la suma de las matrices
    matriz_suma = []
    matriz_suma.append([matriz_1[0][0] + matriz_2[0][0],matriz_1[0][1] + matriz_2[0][1]])
    matriz_suma.append([matriz_1[1][0] + matriz_2[1][0],matriz_1[1][1] + matriz_2[1][1]])
    return matriz_suma

def dividir_matrices(matriz,n):
    i=0
    A=[]
    B=[]
    C=[]
    D=[]
    for fila in matriz:
        if(i<(n/2)):
            A.append(fila[:int((n/2))])
            B.append(fila[int((n/2)):])
            i+=1
        else:
            C.append(fila[:int((n/2))])
            D.append(fila[int((n/2)):])
    return(A,B,C,D)
            
def strassen(m1,m2,n):
    if (n == 1):
        return [m1[0][0]*m2[0][0]]

    elif (n == 2): #multiplica matrices 2x2
        a = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]
        b = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
        c = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]
        d = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
        return [[a,b],[c,d]]  #retorna matriz multiplicada

    else:       # divide matrices en cuadrantes
        A,B,C,D = dividir_matrices(m1,n)
        E,F,G,H = dividir_matrices(m2,n)
        #   ahora hay que hacer la suma de los cuadrantes 
        P1 = sum_matrices(strassen(A,E,n/2), strassen(B,G,n/2))
        P2 = sum_matrices(strassen(A,F,n/2), strassen(B,H,n/2))
        P3 = sum_matrices(strassen(C,E,n/2), strassen(D,G,n/2))
        P4 = sum_matrices(strassen(C,F,n/2), strassen(D,H,n/2))
        return P1,P2,P3,P4

P1,P2,P3,P4 = strassen(matriz_1,matriz_2,n)

# entregar bien la matriz resultante, primera linea N  y M (filas y columnas), combinar
#print(P1)

matriz_final = []
matriz_final.append(P1[0]+P2[0])
matriz_final.append(P1[1]+P2[1])
matriz_final.append(P3[0]+P4[0])
matriz_final.append(P3[1]+P4[1])

print(str(k*n) + " "+ str(k*n))
#print(matriz_final)
for i in range(len(matriz_final)):
    print(*matriz_final[i])