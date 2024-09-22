import time
def medir_tiempo(funcion1):
    def funcion2(*args, **kwargs):
        inicio=time.time()
        resultado=funcion1(*args, **kwargs)
        fin=time.time()
        tiempo_total=fin-inicio
        print("El tiempo total de ejecucion fue de: {}".format(tiempo_total))
        return resultado
    return funcion2

@medir_tiempo
def suma_elementos(*args):
    suma=sum(args)
    print("La suma de los elementos es {}".format(suma))

suma_elementos(1,2,3,4,5,6)
suma_elementos(13,42,12,52,32,66)
suma_elementos(4,124,521,23,52,33)