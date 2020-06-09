
#1) ordenar los datos de cada relación y guardarlos en memoría
#2) encontrar los atributos en común que tienen las 2 relaciones (A-B / B-C)
#3) comparar las tuplas y buscar las que tengan el atributo igual
n_R = int(input())
atributos_R = list(input().rstrip().split(" "))
print(atributos_R)
    


#"0 1" -> (0,1)

# 2
# 0 1 -> (0,1)
# 7
# 1 2
# 2 4
# 4 1
# 5 2 ---> [[1,2],[2,4]...]
# 4 5
# 3 4
# 3 5
# 2
# 1 2
# 3
# 3 1
# 2 3
# 5 3
# 3
# 2 3 4
# 2
# 2 5 6
# 6 7 8

def busqueda(pos_atr_R, pos_atr_S, lista_R, lista_S, atr_R, atr_S):
    lista_T = []
    for t_R in lista_R:
        for t_S in lista_S:
            if (t_R[pos_atr_R] == t_S[pos_atr_S]):
                temp = t_R.copy()
                temp2 = t_S.copy()
                del temp2[pos_atr_S:(pos_atr_S+1)]
                lista_T.append(temp + temp2)
                print(t_R,t_S)
    print(lista_T)


def similares(lista_R, lista_S, atr_R, atr_S, n_R, n_S):
    comun = []
    for i in range(n_R):
        for j in range(n_S):
            if (atr_R[i]==atr_S[j]) :
                busqueda(i,j,lista_R, lista_S, atr_R, atr_S)
                comun.append(atr_R[i])
    print(comun)





similares( [[1,2],[2,3]] , [[2,1,5],[2,3,10]] , [0,1] , [1,2,3] , 2 , 3)
#buscar cuando tienen + de 1 columna en comun
        

        