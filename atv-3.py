import time

def contagem_regressiva(segundos):
    while segundos:
        print(f"Tempo restante: {segundos}s")
        time.sleep(1)
        segundos -= 1
    print(f"\nTempo esgotado!\n")

segundos = int(input("Digite o número de segundos para a contagem regressiva: "))
contagem_regressiva(segundos)