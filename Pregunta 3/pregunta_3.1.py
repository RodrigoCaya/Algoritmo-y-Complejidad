def crearMatriz():
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

    return matriz_1,matriz_2,n,k


def combinar(C1, C2, C3, C4): # combina cuatro matrices en una NO USAR LEN
    p = len(C1)*2 #no usar len
    matriz=[]
    for fila in range(p):       # creamos una matriz del doble de dimensiones y llenamos con ceros
        lista = []
        for columna in range(p):
            lista.append(0)
        matriz.append(lista)

    for i in range(len(C1)):    #rellenamos matriz con valores de las matrices C1, C2, C3 y C4
            for j in range(len(C1)):
                matriz[i][j] = C1[i][j] #primer cuadrante
                matriz[i][j+len(C1)] = C2[i][j] #segundo cuadrante
                matriz[i+len(C1)][j] = C3[i][j] #tercer cuadrante
                matriz[i+len(C1)][j+len(C1)] = C4[i][j] #cuarto cuadrante
    return matriz
   
def sum_matrices(m1,m2): #parametros: dos matrices y retorna la suma de las matrices 
    if type(m1) == int:
        suma = m1 + m2
    else:
        suma = []
        for i in range(len(m1)):
            lista = []
            for j in range(len(m1[0])):
                lista.append(m1[i][j] + m2[i][j])
            suma.append(lista)
    return suma

def res_matrices(m1,m2): #parametros: dos matrices y retorna la resta de las matrices 
    if type(m1) == int:
        resta = m1 - m2
    else:
        xd = len(m1[0])
        resta = []
        for i in range(len(m1)):
            lista = []
            for j in range(xd):
                lista.append(m1[i][j] - m2[i][j])
            resta.append(lista)
    return resta

def dividir_matrices(matriz,n):     #ok
    i=0
    A=[]
    B=[]
    C=[]
    D=[]
    for fila in matriz:
        if(i<(n/2)):
            A.append(fila[:int((n/2))]) #puede ser de más
            B.append(fila[int((n/2)):])
            i+=1
        else:
            C.append(fila[:int((n/2))])
            D.append(fila[int((n/2)):])
    return(A,B,C,D)
            
def strassen(m1,m2,n):
    if (n == 1):
        total = [[0]]
        total [0][0] = m1[0][0]*m2[0][0]    
        return total

    else:       # divide matrices en cuadrantes
        A,B,C,D = dividir_matrices(m1,n)
        E,F,G,H = dividir_matrices(m2,n)
        
        P1 = strassen(sum_matrices(A,D), sum_matrices(E,H),n/2)
        P2 = strassen(sum_matrices(C, D), E,n/2)
        P3 = strassen(A, res_matrices(F, H),n/2)
        P4 = strassen(D, res_matrices(G, E),n/2)
        P5 = strassen(sum_matrices(A, B), H,n/2)
        P6 = strassen(res_matrices(C, A), sum_matrices(E, F),n/2)
        P7 = strassen(res_matrices(B, D), sum_matrices(G, H),n/2)
        
        C1 = sum_matrices(res_matrices(sum_matrices(P1,P4),P5),P7)
        C2 = sum_matrices(P3,P5)
        C3 = sum_matrices(P2,P4)
        C4 = sum_matrices(res_matrices(sum_matrices(P1, P3), P2), P6)

        c = combinar(C1,C2,C3,C4)       #los parametros son las matrices a combinar en una matriz del doble de sus dimensiones
        
        return c



M1,M2,n,k = crearMatriz()
M = strassen(M1,M2,n)

print(M)