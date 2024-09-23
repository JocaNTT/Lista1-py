def calcular_calorias(atividade, tempo):
    if atividade == "caminhada":
        return tempo * 5
    elif atividade == "corrida":
        return tempo * 10
    elif atividade == "ciclismo":
        return tempo * 8
    else:
        return None

atividade = input("Informe o tipo de atividade (caminhada, corrida ou ciclismo): ").lower()
tempo = int(input("Informe o tempo em minutos: "))

calorias_queimadas = calcular_calorias(atividade, tempo)

if calorias_queimadas is not None:
    print(f"Você queimou {calorias_queimadas} calorias durante {tempo} minutos de {atividade}.")
else:
    print("Atividade inválida.")