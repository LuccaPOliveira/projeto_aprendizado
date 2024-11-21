#Variáveis
idade = 28
nome = 'Lucca'
sobrenome = 'Piasseta de Oliveira'

print('Aprendendo Python e Git')
print('Me chamo',nome,sobrenome)
print('Eu tenho {} anos'.format(idade))

#Operações
idadeNova = idade + 1

print('Em janeiro farei {} anos'.format(idadeNova))

#Listas
lista = [1,2,3,4,5]

print(lista)

vontade = input('O que você quer comer?')

if vontade == 'Lanche':
    print('Vá ao Méqui')
    print('Coma um lanche')
elif vontade == 'Pizza':
    print('Vá ao Hut')
    print('Coma uma pizza')
elif vontade == 'Mexicano':
    print('Vá ao Gua.co')
    print('Coma um burrito')
else:
    print('Coma um miojo em casa mesmo!')
print('Fome saciada!')

#Desenvolver um programa para um depósito de bebidas que valide venda de bebidas para maiores de idade (maior ou igual 18 anos)
#no mercado, o programa deve receber do usuário os valores do nome e ano que ele nasceu e retornar se ele pode comprar bebidas.

import datetime

today = datetime.date.today()
year = today.year
nomeUsuario = input('Digite seu nome: ')
anoUsuario = int(input('Digite o ano em que nasceu: '))
idadeUsuario = year - anoUsuario

print('Você tem {} anos'.format(idadeUsuario))
if idadeUsuario >= 18:
  print('Permitida a compra de bebidas alcoólicas')
else:
  print('Compra de bebidas alcoólicas não permitida')

#Pergunte para o usuário de quantos números ele quer tirar a média e tire a média desses números

qtd = int(input('De quantos números você quer tirar a média? '))
passo = range(1,qtd+1)
soma = 0

for i in passo:
  n = float(input('Digite o {}º número: '.format(i)))
  soma += n
media = soma / i
print('A média dos {} números é {}'.format(i,media))