
def busqueda(comun, lista_R, lista_S):
    lista_T = []
    for t_R in lista_R:
        for t_S in lista_S:
            temp2 = t_S.copy()
            flag = 0
            for t_comun in comun:
                pos_atr_R = t_comun[1]
                pos_atr_S = t_comun[2]
                if (t_R[pos_atr_R] == t_S[pos_atr_S]):
                    del temp2[pos_atr_S:(pos_atr_S+1)]
                else: 
                    flag = 1
            if (flag == 0):
                lista_T.append(t_R + temp2)
    print(lista_T)


def similares(lista_R, lista_S, atr_R, atr_S, n_R, n_S):
    comun = []
    for i in range(n_R):
        for j in range(n_S):
            if (atr_R[i]==atr_S[j]) :
                comun.append([atr_R[i],i,j])
    busqueda(comun,lista_R,lista_S)

#Guardando datos de relacion R
n_atributos_R = int(input())
atributos_R = list(input().rstrip().split(" "))
n_tuplas_R = int(input())
tuplas_R = []
for i in range(n_tuplas_R):
        tuplas_R.append(list(input().rstrip().split(" ")))

#Guardando datos de relacion S
n_atributos_S = int(input())
atributos_S = list(input().rstrip().split(" "))
n_tuplas_S = int(input())
tuplas_S = []
for i in range(n_tuplas_S):
        tuplas_S.append(list(input().rstrip().split(" ")))

similares(tuplas_R,tuplas_S,atributos_R,atributos_S,n_atributos_R,n_atributos_S)
        

        