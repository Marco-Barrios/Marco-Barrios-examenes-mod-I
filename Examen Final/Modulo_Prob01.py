def numeros(a,b,c,d,e,f,g,h,i,j):
    lista_numeros=[a,b,c,d,e,f,g,h,i,j]
    print("La lista de numeros es: {}".format(lista_numeros))
    return lista_numeros
def norepetidos(lista_numeros):
    lista_norepetidos=[]
    for numero in lista_numeros:
        if lista_numeros.count(numero)==1:
            lista_norepetidos.append(numero)
    print("La lista de numeros no repetidos es: {}".format(lista_norepetidos))
    return lista_norepetidos
def ordenar(lista_norepetidos):
    lista_ordenada=sorted(lista_norepetidos)
    print("La lista ordenada es: {}".format(lista_ordenada))
    return lista_ordenada
def mayor_par(lista_ordenada):
    numero_mayor=max(lista_ordenada)
    return numero_mayor
