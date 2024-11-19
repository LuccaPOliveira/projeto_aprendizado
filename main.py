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
