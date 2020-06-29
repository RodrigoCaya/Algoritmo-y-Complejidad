def crearMatriz():
    linea_1 = input().rstrip().split(" ")
    n = int(linea_1[0])
    k = int(linea_1[1])
    matriz_1 = []
    matriz_2 = []
    #guardamos valores primera matriz
    for i in range(n):
        fila = list(map(int, input().rstrip().split(" ")))
        matriz_1.append(fila)

    for i in range(k * n):
        fila = list(map(int, input().rstrip().split(" ")))
        matriz_2.append(fila)

    return matriz_1,matriz_2,n,k

def matriz_ceros(dim):
    matriz = []
    for i in range(dim):
        fila = []
        for j in range(dim):
            fila.append(0)
        matriz.append(fila)
    return matriz

def potencia_mas_cercana(kn):
    for i in range(kn):
        if (2**i >= kn):
            return 2**i

    
def rellenar_matriz(matriz,k ,n):
    dim = potencia_mas_cercana(k*n)
    matriz_retorno = matriz_ceros(dim)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_retorno[i][j] = matriz[i][j]
    return matriz_retorno,dim

def sacar_ceros(matriz,k ,n):
    matriz_final = matriz_ceros(n)
    for i in range(n):
        for j in range(n):
            matriz_final[i][j] = matriz[i][j]
    
    return matriz_final

def metodoTradicional(a, b): 
    if len(a[0]) != len(b): 
        return "Las matrices no son de la forma m*n y n*p"
    else:
        matriz_multiplicada = matriz_ceros(len(a))
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    matriz_multiplicada[i][j] += a[i][k]*b[k][j]
    return matriz_multiplicada


def combinar(C1, C2, C3, C4): # combina cuatro matrices en una NO USAR LEN
    p = len(C1)*2 #no usar len
    o = len(C1)
    matriz=[]
    for fila in range(p):       # creamos una matriz del doble de dimensiones y llenamos con ceros
        lista = []
        for columna in range(p):
            lista.append(0)
        matriz.append(lista)

    for i in range(o):    #rellenamos matriz con valores de las matrices C1, C2, C3 y C4
            for j in range(o):
                matriz[i][j] = C1[i][j] #primer cuadrante
                matriz[i][j+o] = C2[i][j] #segundo cuadrante
                matriz[i+o][j] = C3[i][j] #tercer cuadrante
                matriz[i+o][j+o] = C4[i][j] #cuarto cuadrante
    return matriz
   
def sum_matrices(m1,m2): #parametros: dos matrices y retorna la suma de las matrices 
    if type(m1) == int:
        suma = m1 + m2
    else:
        suma = []
        largo_m1 = len(m1)
        largo_m1_columnas = len(m1[0])
        for i in range(largo_m1):
            lista = []
            for j in range(largo_m1_columnas):
                lista.append(m1[i][j] + m2[i][j])
            suma.append(lista)
    return suma

def res_matrices(m1,m2): #parametros: dos matrices y retorna la resta de las matrices 
    if type(m1) == int:
        resta = m1 - m2
    else:
        resta = []
        for i in range(len(m1)):
            lista = []
            for j in range(len(m1[0])):
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

#print(M1)
#print(M2)

matriz_1,N = rellenar_matriz(M1,k,n)
matriz_2,N = rellenar_matriz(M2,k,n)


strass = strassen(matriz_1,matriz_2,N)
final = sacar_ceros(strass,k,n)

print(str(len(final)) + " " + str(len(final[0])))
for i in range(len(final)):
    print(*final[i])

#print(metodoTradicional(M1,M2))
