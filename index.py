# Pedro Hugo e Cinthia Katiane
# Sistema Bancário - Python 

Contas = {'cod' : [], 'saldo' : []}
Trans = {'cod' : [], 'origem' : [], 'destino' : [], 'valor' : []}
Clientes = {'cod' : [], 'nome' : [], 'cc' : []}
numClientes = 0

play_in_proccess = True

while play_in_proccess:
    print ("")
    print ("1 - Menu - Contas Clientes")
    print ("2 - Menu - Transferências")
    print ("3 - Sair")

    menuop = input("Digite o número da opçao desejada: ")

    if (menuop == '3') :
      play_in_proccess = False
        
    elif (menuop == '1') :
      play_in_proccess1 = True
      while play_in_proccess1:
        print("")
        print("1 - Inserir novo cliente")
        print("2 - Consultar conta de um cliente")
        print("3 - Atualizar cadastro de um cliente")
        print("4 - Remover um clientes")
        print("5 - Imprimir lista de clientes")
        print("6 - Voltar")

        menuCliente = input ("\nDigite o numero da opçao desejada: ")

        if (menuCliente == '6') :
            play_in_proccess1 = False

        ## 1 - Inserir novo cliente
        if (menuCliente == '1') :
  
          cod = input ("\nInforme o codigo do cliente: ")
          nome = input ("Informe o nome do cliente: ")
          cc = input ("Informe o numero da conta corrente do cliente: ") 

          #verificação de contas com mesmo código // cinthia

          Clientes['cod'].append(cod)
          Clientes['nome'].append(nome)
          Clientes['cc'].append(cc)
          Contas['cod'].append(cc)
          Contas['saldo'].append(0.0)

          numClientes = numClientes + 1


        ## 2 - Consultar dados de um cliente 
        elif (menuCliente == '2') :

          consultar = input ("\nInforme o codigo do cliente: ")
          consultarV = consultar in Clientes['cod']
          
          if consultarV == True:  
            pos = Clientes['cod'].index(consultar)
            print("Codigo \t Nome \t Conta")
            print("{0} \t {1} \t {2}".format(Clientes['cod'][pos],Clientes['nome'][pos],Clientes['cc'][pos],Contas['saldo'][pos]))

          else:
            print("Codigo invalido!!!")

        ## 3 - Atualizar cadastro de um cliente 
        elif (menuCliente == '3') :
            
          consultar = input ("\nInforme o codigo do cliente: ")
          consultarV = consultar in Clientes['cod']
            
          if consultarV == True:
                
            newnome = input ("Informe o novo nome do cliente: ")
            
            pos = Clientes['cod'].index(consultar)
            
            Clientes['nome'][pos] = newnome

            print("\nDados atualizados!!!\n")

          else:
            print("Codigo invalido!!!")

        ## 4 - Remover um clientes 
        elif (menuCliente == '4') :
            
          consultar = input ("\nInforme o codigo do cliente: ")
          consultarV = consultar in Clientes['cod']
          
          if consultarV == True:
              
            pos = Clientes['cod'].index(consultar)
            Clientes['cod'].pop(pos)
            Clientes['nome'].pop(pos)
            Clientes['cc'].pop(pos)
            Contas['cod'].pop(pos)
            Contas['saldo'].pop(pos)

            numClientes = numClientes - 1
            print("Removido com sucesso")

          else:
            print("Codigo invalido!!!")

        ## 5 - Imprimir lista de clientes 
        elif (menuCliente == '5') : 
          print("Codigo \t Nome \t \t Conta \t Saldo")
          print()
          
          for i in range(numClientes):              
              
              print("{0} \t {1} \t {2} \t {3}".format(Clientes['cod'][i],Clientes['nome'][i],Clientes['cc'][i], Contas['saldo'][i]))

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
            consultarV = consultar in Contas['cod']
            
            if consultarV == True:
              pos = Contas['cod'].index(consultar)
              deposito = input ("\nInforme o valor do deposito: ")
              deposito = float(deposito)
              valor = Contas['saldo'][pos]
              valor = valor + deposito
              Contas['saldo'][pos] = valor
            else:
              print("Conta nao existe!!")


            # Lista de trans

          elif (opmenu == '2') :
            consultar = input ("\nInforme o codigo da conta em que deseja realizar o saque: ")
            consultarV = consultar in Contas['cod']
            
            if consultarV == True:

              pos = Contas['cod'].index(consultar)
              saque = input ("\nInforme o valor do saque: ")
              saque = float(saque)
              valor = Contas['saldo'][pos]

              if valor > saque:
                valor = valor - saque
                Contas['saldo'][pos] = valor
              else:
                print("Saldo insuficiente!!")

            else:
              print("Conta nao existe!!")
          
          elif (opmenu == '3') :
            print ("Em desenvolvimento")

print ("Finalizando...")