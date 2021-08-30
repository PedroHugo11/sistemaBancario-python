class Conta():
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0     

    def sacar(self, valor):
        self.saldo -= valor    

    def depositar(self,valor):
        self.saldo += valor