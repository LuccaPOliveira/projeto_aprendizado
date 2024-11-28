# Declarando a lista
clientes = []

# Direciona o código para criação de novos cadastros ou busca de cadastros existentes
while True:
  opcao = input("Digite 1 para cadastrar um cliente, 2 para pesquisar um cliente ou 0 para sair: ")

# Solicita as informações de novos clientes e as armazena na lista criada anteriormente
  if opcao == '1':
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    clientes.append([nome, email, telefone, idade])
    print("Cliente cadastrado com sucesso!")

# Realiza a procura de cadastros existentes com base no e-mail
  elif opcao == '2':
    email_pesquisa = input("Digite o email do cliente que deseja pesquisar: ")
    cliente_encontrado = False
    for cliente in clientes:
      if cliente[1] == email_pesquisa:
        print("Nome:", cliente[0])
        print("Email:", cliente[1])
        print("Telefone:", cliente[2])
        print("Idade:", cliente[3])
        cliente_encontrado = True
        break
    if not cliente_encontrado:
        print("Cliente não encontrado.")

#Finaliza o programa
  elif opcao == '0':
    break
  else:
    print("Opção inválida.")