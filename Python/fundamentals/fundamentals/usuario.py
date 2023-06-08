class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    # los asignamos en consecuencia
        self.name = name
        self.email = email_address
    # el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount	# la cuenta del ususario específico desciende en la cantidad del valor recibido
    def mostrar_balance_usuario(self):
        print(self.name + ", Balance: $" + str(self.balance_cuenta)) # se muestra el balance
    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount

melanie = Usuario("Melanie Veliz", "melanie@python.com")
melanie.hacer_depósito(100)
melanie.hacer_depósito(200)
melanie.hacer_depósito(300)
melanie.hacer_retiro(100)
melanie.mostrar_balance_usuario()

esteban = Usuario("Esteban Salas", "esteban@python.com")
esteban.hacer_depósito(100)
esteban.hacer_depósito(200)
esteban.hacer_retiro(50)
esteban.hacer_retiro(50)
esteban.mostrar_balance_usuario()

maria = Usuario("Maria Veliz", "maria@python.com")
maria.hacer_depósito(500)
maria.hacer_retiro(50)
maria.hacer_retiro(100)
maria.hacer_retiro(200)
maria.mostrar_balance_usuario()

melanie.transfer_dinero(maria,50)
melanie.mostrar_balance_usuario()
maria.mostrar_balance_usuario()



