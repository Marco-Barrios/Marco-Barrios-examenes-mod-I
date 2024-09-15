class BilleteraElectronica:
    def __init__(self, nombre_titutar, apellido_titular, saldo_soles, saldo_dolares):
        self.nombre_titutar = nombre_titutar
        self.apellido_titular = apellido_titular
        self.saldo_soles = saldo_soles
        self.saldo_dolares = saldo_dolares
    def transferir(self):
        monto=int(input("Ingrese el monto a transferir: "))
        cuenta_transf=(input("Si quiere transferir de soles a dolares escriba sol_dol, caso contrario escriba dol_sol: "))
        if cuenta_transf=="sol_dol":
            if monto<=self.saldo_soles:
                dif_sol=self.saldo_soles - monto
                nuevo_dol=self.saldo_dolares + (monto/3.75)
                print("Su nuevo saldo en su cuenta soles es: {}".format(dif_sol))
                print("Su nuevo saldo en su cuenta en dolares es: {}".format(nuevo_dol))
            else:
                print("No posee saldo suficiente para realizar la transferencia")
        elif cuenta_transf=="dol_sol":
            if monto<=self.saldo_dolares:
                dif_dol=self.saldo_dolares - monto
                nuevo_sol=self.saldo_soles + (monto*3.75)
                print("Su nuevo saldo en su cuenta en dolares es: {}".format(dif_dol))
                print("Su nuevo saldo en su cuenta en soles es: {}".format(nuevo_sol))
        else:
            print("Ingrese el texto correctamente")
    def retiro(self):
        monto_retiro=int(input("Ingrese el monto a retirar: "))
        seleccion_cuenta=input("Si desea retirar de su cuenta en soles escriba soles, si desea retirar de su cuenta en dolares escriba dolares: ")
        if seleccion_cuenta=="soles":
            if monto_retiro<=self.saldo_soles:
                sol_actualizado=self.saldo_soles - monto_retiro
                print("Su retiro se efectuo exitosamente")
                print("Su nuevo saldo en su cuenta en soles es: {}".format(sol_actualizado))
            else:
                print("No posee saldo suficiente para realizar el retiro")
        if seleccion_cuenta=="dolares":
            if monto_retiro<=self.saldo_dolares:
                dol_actualizado=self.saldo_dolares - monto_retiro
                print("Su retiro se efectuo exitosamente")
                print("Su nuevo saldo en su cuenta en dolares es: {}".format(dol_actualizado))

cuenta1=BilleteraElectronica("Marco", "Barrios", 1000, 500)
cuenta1.transferir()
cuenta1.retiro()







