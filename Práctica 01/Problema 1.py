nombre = "Marco Barrios"
compañia="Movistar"
salario = 1000
edad = "24"
edad_conv=int(edad)
print("La variable nombre es de tipo:")
print(type(nombre))
print("La variable compañia es de tipo:")
print(type(compañia))
print("La variable salario es de tipo:")
print(type(salario))
print("La variable edad es de tipo:")
print(type(edad))
print("La variable edad_conv es de tipo:")
print(type(edad_conv))

if edad_conv>30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
else:
    print("Usted tiene un bono de 5% en el mes de diciembre")
bono_final=pow(salario,2) + 0.05*salario

print("Su bono final es de {}".format(bono_final))