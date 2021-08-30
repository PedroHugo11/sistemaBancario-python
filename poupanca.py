from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self,codigo):
        Conta.__init__(self, codigo)

    def renderJuros(self, taxa):
        rendimento = self.saldo*(taxa/100)
        self.saldo += rendimento
        print ("O rendimento da conta foi de: ", rendimento)
        print ("O saldo final é: ", self.saldo)
