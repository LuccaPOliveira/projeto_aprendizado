#Declarando minhas variáveis
t1 = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Salgado', 4.5, 'Paçoca', 0.5, 'Bolo', 5.4)
l1 = []
soma = 0

#Criando a visualização do cardápio
print('-'*28)
print('-'*10+'Cardápio'+'-'*10)
print('-'*28)
for i in range(0,len(t1),2):
  print('{:17} : R$ {:5.2f}'.format(t1[i],t1[i+1]))
print('-'*28)
print()

#Recebendo o pedido, mantendo uma lista de tudo que o cliente selecionou e calculando o valor total
while True:
  item = input('O que deseja? ')
  l1.append(item)
  soma += t1[t1.index(item)+1]
  continua = input('Quer continuar comprando? (s/n)')
  if continua == 'n':
    break

#Exibindo os itens pedidos e o valor final
print(f'Você pediu {l1} e o valor final do seu pedido é R${soma:.2f}')