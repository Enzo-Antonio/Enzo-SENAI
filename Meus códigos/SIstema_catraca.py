#-*-coding:UTF-8-*-
print("Aproxime o cartão")
saldo=float(input("Saldo disponível: "))
if saldo < 3.80:
    print("Saldo insuficiente")
else:
    novo_sal=saldo - 3.80
    print(f"Seu saldo atual é de {novo_sal}")
