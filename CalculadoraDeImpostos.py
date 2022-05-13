#Calculadora de Impostos: você foi viajar e deseja saber quanto terá de pagar 
# de imposto aplicado nas suas compras da viagem.

print('Bem-vinde à Calculadora de impostos!')
preco = 0
soma = 0
contador = 0

imposto = int(input('Qual a porcentagem de imposto sob o produto?'))
produtos = int(input('Quantos produtos você deseja registrar?'))

while contador < produtos:
    contador = contador + 1
    preco = float(input(f'Informe o preço do {contador}º produto:'))
    soma = preco + soma
resultado = soma * imposto / 100
print(f'Você gastou um total de {soma} reais. O total a pagar de imposto é de {resultado} reais.')
print('Obrigade por usar a Calculadora de Impostos! \nAté mais.')
