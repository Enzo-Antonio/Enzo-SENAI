#-*-coding:UTF-8-*-
num=float(input('Digite o valor do primeiro produto: '))
num2=float(input('Digite o valor do segundo produto: '))
num3=float(input('Digite o valor do terceiro produto: '))
L=[num, num2, num3]
resul=num+num2+num3
print(f'Quantidade de produtos: {len(L)}')
print(f'Valor dos produtos: {L}')
print(f'Valor total: {resul}')