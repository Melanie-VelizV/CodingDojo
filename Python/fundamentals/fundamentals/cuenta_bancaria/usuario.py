from cuenta_bancaria import CuentaBancaria

class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!

    def __init__(self , name, email_address):
    # los asignamos en consecuencia
        self.name = name
        self.email = email_address
        self.cuenta = CuentaBancaria(tasa_interes=2, balance=0)	# añadió esta línea

    # agregando el método de depósito
    def hacer_deposito(self, cuenta,amount):	# toma un argumento que es el monto del depósito
        cuenta.cuenta.deposito( amount)
        return cuenta	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
    def hacer_retiro(self, cuenta,amount):
        cuenta.cuenta.retiro(amount)	# la cuenta del ususario específico desciende en la cantidad del valor recibido
        return cuenta
    def mostrar_balance_usuario(self,cuenta):
        print ("Balance de ",cuenta.name, "es de:")
        cuenta.cuenta.mostrar_info_cuenta(cuenta) # se muestra el balance
        return cuenta
    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount

melanie = Usuario("Melanie Veliz", "melanie@python.com")
melanie.hacer_deposito(melanie,100).hacer_retiro(melanie,100).mostrar_balance_usuario(melanie)


maria = Usuario("Maria Veliz", "maria@python.com")
maria.hacer_deposito(maria,500).hacer_retiro(maria,50).hacer_deposito(melanie,100).mostrar_balance_usuario(melanie).mostrar_balance_usuario(maria)

