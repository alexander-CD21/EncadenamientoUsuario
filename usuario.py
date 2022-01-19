class Usuario:

    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.balance=0
    def hacerDeposito(self,amount):
        self.balance=self.balance+amount
        return self
    def hacerRetiro(self,amount):
        self.balance=self.balance - amount
        return self
    def mostrarBalanceUsuario(self):
        print(f"Usuario: {self.nombre} y balance: {self.balance}")
        return self
    def transferirDinero(self,amount1,cuenta):
        self.balance-=amount1
        cuenta.balance+=amount1
        self.mostrarBalanceUsuario()
        cuenta.mostrarBalanceUsuario()
        return self
