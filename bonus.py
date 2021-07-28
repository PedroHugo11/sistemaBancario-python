from conta import Conta
from bonus import ContaBonus

class ContaBonus(Conta):
    def _init_(self,codigo):
        Conta._init_(self, codigo)
        self.bonus = 10

    def depositar(self,valor):
        self.saldo += valor
        bonus = int(valor/100)
        self.bonus += bonus
        print ("Você acabou de receber mais ", bonus, " pontos")
        print ("O seu total de pontos é: ", self.bonus)

    def depositoEspecial(self,valor):
        self.saldo += valor
        bonus = int(valor/200)
        self.bonus += bonus
        print ("Você acabou de receber mais ", bonus, " pontos")
        print ("O seu total de pontos é: ", self.bonus)