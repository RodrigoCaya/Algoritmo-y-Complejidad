def verTope(horario_1,horario_2):   
    if (horario_2[0] <= horario_1[1] and horario_2[0] >= horario_1[0]):
        return True

    elif (horario_2[1] >= horario_1[0] and horario_2[1] <= horario_1[1]):
        return True

    else:
        return False

def obtenerDatos():
    cant_horarios = int(input())
    horarios = []
    for i in range(cant_horarios):
        horarios.append(tuple(map(int,input().rstrip().split(" ")))) # Convertimos los valores a una tupla y los almacenamos en una lista
    return horarios

def ordenar(horarios):
    i = 0
    for par_horario in horarios:
        rango = par_horario[1] - par_horario[0]
        horarios[i] = (rango,par_horario[0],par_horario[1])
        i+=1
    horarios = sorted(horarios)
    i=0
    for trio_horario in horarios:
        horarios[i] = (trio_horario[1],trio_horario[2])
        i+=1
    return horarios

def alg_greedy(horarios):
    lista_final = [horarios[0]]
    n = len(horarios)
    for i in range(1,n):
        flag = True
        for par_final in lista_final:
            if (verTope(horarios[i],par_final)):
                flag = False
                break
        if flag:
            lista_final.append(horarios[i])
    return sorted(lista_final)
            

horarios = obtenerDatos()
horarios = ordenar(horarios)

final = alg_greedy(horarios)
print(len(final))
for horario in final:
    print(str(horario[0]),end='')
    print(" ",end='')
    print(str(horario[1]),end='')
    print("\n",end='')