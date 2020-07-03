import fileinput
arcos = []
for line in fileinput.input():
    arcos.append(line.rstrip().split()) #toma de datos desde stdin
grafo = []
for arco in arcos:
    if arco not in grafo:
        grafo.append(arco)  #se agregan arcos a una lista, excluye si salen repetidos

def busqueda(grafo):
    triangulos = []
    for arco_1 in grafo: #revisa arco por arco
        grafo_temp = grafo.copy() #generamos una copia al grafo
        grafo_temp.remove(arco_1)  #quitamos el grafo sobre el que iteramos de la copia
        for arco_2 in grafo_temp: #vamos por el siguiente arco
            if (arco_1[1] == arco_2[0]): # se cumple si hay "join" entre el atributo 2 del arco_1 y
                grafo_temp.remove(arco_2) # el atributo 1 del arco_2, y sacamos al arco_2 de la lista temporal
                for arco_3 in grafo_temp:
                    if (arco_2[1] == arco_3[0] and arco_1[0] == arco_3[1]): #idem a lo anterior, solo que ademas comapra al arco_3 con el 1 y el 2
                        ciclo = arco_1 + list(arco_3[0]) #entonces hay un ciclo
                        ciclo.sort()
                        if ciclo not in triangulos: #esto es para excluir repetidos
                            triangulos.append(ciclo)
    print(len(triangulos))

busqueda(grafo)