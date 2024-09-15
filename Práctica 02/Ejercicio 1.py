class Persona:
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
        self.saldo=int(input("Ingrese su saldo: "))
        self.nacionalidad="Peruana"
    def cumpleaños(self):
        self.edad+=1
    def aumentoSueldo(self):
        self.saldo*=1.3
        print("Su nuevo sueldo es: {}".format(self.saldo))
    def edad_años(self):
        año=int(input("Ingrese un año: "))
        edad_futura=self.edad + (año-2024)
        print("Su edad en el año {} será de {} años".format(año,edad_futura))

persona1=Persona()
persona1.aumentoSueldo()
persona1.edad_años()

persona2=Persona()
persona2.aumentoSueldo()
persona2.edad_años()

