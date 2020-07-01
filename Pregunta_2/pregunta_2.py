import fileinput
arcos = []
for line in fileinput.input():
    arcos.append(line.rstrip().split())
grafo = []
for arco in arcos:
    if arco not in grafo:
        grafo.append(arco) 

def busqueda(grafo):
    triangulos = []
    for arco_1 in grafo:
        grafo_temp = grafo.copy()
        grafo_temp.remove(arco_1)
        for arco_2 in grafo_temp:
            if (arco_1[1] == arco_2[0]):
                grafo_temp.remove(arco_2)
                for arco_3 in grafo_temp:
                    if (arco_2[1] == arco_3[0] and arco_1[0] == arco_3[1]):
                        ciclo = arco_1 + list(arco_3[0])
                        ciclo.sort()
                        if ciclo not in triangulos:
                            triangulos.append(ciclo)
    print(len(triangulos))

busqueda(grafo)