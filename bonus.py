from conta import Conta

class ContaBonus(Conta):
    def __init__(self,codigo):
        Conta.__init__(self, codigo)
        self.bonus = 10

    def depositar(self,valor):
        self.saldo += valor
        bonus = int(valor/100)
        self.bonus += bonus
        print ("Você acabou de receber mais ", bonus, " pontos")
        print ("O seu total de pontos é: ", self.bonus)

    def depositoEspecial(self,valor):
        self.saldo += valor
        bonus = int(valor/150)
        self.bonus += bonus
        print ("Você acabou de receber mais ", bonus, " ponto(s)")
        print ("O seu total de pontos é: ", self.bonus)