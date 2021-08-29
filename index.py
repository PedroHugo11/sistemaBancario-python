# Pedro Hugo e Cinthia Katiane
# Sistema Bancário - Python 

from conta import Conta
from poupanca import ContaPoupanca

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
          print("2 - Conta poupança")
          tipo = input ("Informe o tipo da conta: ") 
          cod = input ("Informe o numero da conta: ") 
          conta = buscar_conta(cod)
          if tipo == '1':
            if conta:
              print ("Essa conta já existe, tente novamente!")
            else:
              Contas.append(Conta(cod))
          if tipo == '2':
            if conta:
              print ("Essa conta já existe, tente novamente!")
            else:
              Contas.append(ContaPoupanca(cod))

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
          print("4 - Render Juros")
          print("5 - Voltar")

          opmenu = input("\nDigite o numero da opçao desejada: ")        

          if (opmenu == '5') :
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
              saque = input ("\nInforme o valor do deposito: ")
              saque = float(saque)

              if conta and isinstance(conta, ContaPoupanca):
                saldo = conta.saldo - saque
                if saldo < 0:
                  print("Conta Poupança não pode ser negativa")
                else:
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
                destino.depositar(transferencia)
                print("Transferencia efetuada com sucesso")
              else:
                print("Saldo insuficiente!!")
            else :
                print("Conta nao existe!!")

          elif (opmenu == '4') :
            cod = input("\nInforme o codigo da conta em que deseja calcular o rendimento: ")
            conta = buscar_conta(cod)
            if conta and isinstance(conta, ContaPoupanca):
              taxa = input("\nInforme a taxa de rendimento: ")  
              taxa = float(taxa)
              conta.renderJuros(taxa)
            else :
                print("Não é possivel realizar essa operação")

print ("Finalizando...")