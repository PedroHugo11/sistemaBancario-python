# Pedro Hugo e Cinthia Katiane
# Sistema Bancário - Python 

from conta import Conta
from bonus import ContaBonus

Contas = []
play_in_proccess = True

def buscar_conta(codigo):
  for conta in Contas:
    if conta.codigo == codigo:
      return conta

while play_in_proccess:
    print ("")
    print ("1 - Menu - Conta")
    print ("2 - Menu - Operações")
    print ("3 - Sair")

    menuop = input("Digite o número da opçao desejada: ")

    if (menuop == '3') :
      play_in_proccess = False
        

    elif (menuop == '1') :
      play_in_proccess1 = True
      while play_in_proccess1:
        print("")
        print("1 - Cadastrar conta")
        print("2 - Consultar saldo")
        print("3 - Voltar")

        menuCliente = input ("\nDigite o numero da opçao desejada: ")
        
        ## 3 - Voltar
        if (menuCliente == '3') :
            play_in_proccess1 = False

        ## 1 - Inserir nova conta
        if (menuCliente == '1') :

          print("1 - Conta corrente")
          print("2 - Conta Bonus")
          tipo = input ("Informe o tipo da conta: ") 
          cod = input ("Informe o numero da conta: ") 
          conta = buscar_conta(cod)
          if tipo == '1':
            if conta:
              print ("Essa conta já existe, tente novamente!")
            else:
              Contas.append(Conta(cod))
          elif tipo == '2':
            if conta:
              print ("Essa conta já existe, tente novamente!")
            else:
              Contas.append(ContaBonus(cod))

        ## 2 - Consultar saldo
        elif (menuCliente == '2') :
          consultar = input ("\nInforme o numero da conta: ")
          conta = buscar_conta(consultar)
          if conta :
            print ("Saldo: ", conta.saldo)
          else:
            print("Codigo invalido!!!")

    elif (menuop == '2') :
        
        play_in_proccess2 = True
        while play_in_proccess2:
          print("")
          print("1 - Deposito")
          print("2 - Saque")
          print("3 - Transferencia")
          print("4 - Voltar")

          opmenu = input("\nDigite o numero da opçao desejada: ")        

          if (opmenu == '4') :
            play_in_proccess2 = False

          elif (opmenu == '1') :

            consultar = input ("\nInforme o código da conta em que deseja realizar o deposito: ")
            conta = buscar_conta(consultar)
          
            if conta:
              deposito = input ("\nInforme o valor do deposito: ")
              deposito = float(deposito)
              conta.depositar(deposito)
              print("Deposito efetuado com sucesso")
            else:
              print("Conta nao existe!!")

          elif (opmenu == '2') :
            consultar = input ("\nInforme o codigo da conta em que deseja realizar o saque: ")
            conta = buscar_conta(consultar)

            if conta:
              saque = input ("\nInforme o valor do saque: ")
              saque = float(saque)
              conta.sacar(saque)
              print("Saque efetuado com sucesso")
            else:
              print("Conta nao existe!!")

          elif (opmenu == '3') :
            conta_origem = input("\nInforme o codigo da conta de origem da qual deseja realizar a operação: ")
            conta_destino = input("\nInforme o codigo da conta destino para qual deseja realizar a operação: ")

            origem = buscar_conta(conta_origem)
            destino = buscar_conta(conta_destino)

            if origem and destino:
              transferencia = input ("\nInforme o valor da transferencia: ")
              transferencia = float(transferencia)
              if origem.saldo >= transferencia:
                origem.sacar(transferencia)
                if isinstance(destino, ContaBonus):
                  destino.depositoEspecial(transferencia)
                else: 
                  destino.depositar(transferencia)
              else:
                print("Saldo insuficiente!!")
            else :
                print("Conta nao existe!!")

print ("Finalizando...")