import datetime
def conteo(funcion1):
    def funcion2(*args, **kwargs):
        cantidad_parametros=len(args)+len(kwargs)
        if cantidad_parametros>1:
            resultado=funcion1(*args, **kwargs)
            print("La funcion {} fue ejecutada con {} parametros".format(funcion1.__name__,cantidad_parametros))
            return resultado
        else:
            print("Se requiere más de 1 parametro para ejecutar la funcion {}".format(funcion1.__name__))
            return None
    return funcion2

@conteo
def persona(nombre,edad):
    tiempo=datetime.datetime.now()
    hora=tiempo.hour
    minuto=tiempo.minute
    segundo=tiempo.second
    print("Bienvenido {} de {} años. La hora de su registro fue a las {} horas con {} minutos y {} segundos.".format(nombre, edad, hora, minuto, segundo))

@conteo
def media(nota1,nota2,nota3,nota4):
    media_notas=(nota1+nota2+nota3+nota4)/4
    print("La media de sus notas es: {}".format(media_notas))
    return media_notas

persona("Marco",24)
media(16,17,18,15)
persona("Antonio")
