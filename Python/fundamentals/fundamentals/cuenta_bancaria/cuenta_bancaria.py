class CuentaBancaria:
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    cuentas= []

    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self
    
    def mostrar_info_cuenta(self):
        print ("Balance: " + str(self.balance))

    def generar_interes(self):
        interes= self.tasa_interes/100
        self.balance *= 1 + interes
        return self
    
    @classmethod
    def imprimir_info_cuentas(cls):
        for cuenta in cls.cuentas:
            print("Tasa de interés:", cuenta.tasa_interes)
            print("Balance:", cuenta.balance)
            print("---")

melanie = CuentaBancaria(1,100)
melanie.deposito(100).deposito(100).deposito(100).retiro(50).generar_interes().mostrar_info_cuenta()
esteban = CuentaBancaria(2,500)
esteban.deposito(200).deposito(100).retiro(50).retiro(50).retiro(100).retiro(200).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_info_cuentas()
