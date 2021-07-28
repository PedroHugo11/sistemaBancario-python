class Conta():
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0     

    def sacar(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor
        else:
            print("Saldo insuficiente!!")

    def depositar(self,valor):
        self.saldo += valor