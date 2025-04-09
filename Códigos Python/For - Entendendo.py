print("Oi usuário, vamos receber 5 notas suas e fazer sua média!")
cont=0
acum=0
for notas in range(5, 10):
    nota=float(input("Digite sua nota: "))
    acum=acum+nota
    cont=cont+1
print("A sua média será de: ", acum/5)