def calcular_gorjeta(valor_conta, percentual_gorjeta):
    if percentual_gorjeta == 10:
        return valor_conta * 0.10
    elif percentual_gorjeta == 15:
        return valor_conta * 0.15
    elif percentual_gorjeta == 20:
        return valor_conta * 0.20
    else:
        return None
valor_conta = float(input("Informe o valor da conta: R$ "))
percentual_gorjeta = int(input("Informe o percentual de gorjeta (10, 15, 20): "))

gorjeta = calcular_gorjeta(valor_conta, percentual_gorjeta)

if gorjeta is not None:
    total = valor_conta + gorjeta
    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total: R$ {total:.2f}")
else:
    print("Percentual inválido.")