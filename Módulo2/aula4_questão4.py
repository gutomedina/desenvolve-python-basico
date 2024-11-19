def calcular_notas(valor):
    notas_disponiveis = [100, 50, 20, 10, 5, 2, 1]
    resultado = []

    for nota in notas_disponiveis:
        quantidade, valor = divmod(valor, nota)
        resultado.append((nota, quantidade))
    
    return resultado

def formatar_saida(notas):
    for nota, quantidade in notas:
        print(f"{quantidade} nota(s) de R${nota},00")

if __name__ == "__main__":
    valor = int(input())
    notas = calcular_notas(valor)
    formatar_saida(notas)