#-*-coding:UTF-8-*-
print("Isso é uma calculadora, escolha operações e os valores com os quais operar!")
op=input("Digite a operação a ser realizada, + para soma, - para subtração, x para multiplicação e / para divisão: ")
valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))
def soma(x):
    soma = valor1 + valor2
    print(f"{valor1} + {valor2} = {soma}")

if op == "+":
    soma(1)

def sub(x):
    subtra = valor1 - valor2
    print(f"{valor1} - {valor2} = {subtra}")

if op == "-":
    sub(1)

def multi(x):
    multiplicacao = valor1 * valor2
    print(f"{valor1} x {valor2} = {multiplicacao}")

if op == "x":
    multi(1)

def div(x):
    divisao = valor1 / valor2
    print(f"{valor1} : {valor2} = {divisao}")

if op == "/":
    div(1)
    
