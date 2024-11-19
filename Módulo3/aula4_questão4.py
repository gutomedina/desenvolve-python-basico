def calcular_frete(distancia, peso):
    if distancia <= 100:
        custo_por_kg = 1.0
    elif 101 <= distancia <= 300:
        custo_por_kg = 1.5
    else:
        custo_por_kg = 2.0

    frete = custo_por_kg * peso

    if peso > 10:
        frete += 10  # Taxa adicional para pacotes com peso superior a 10 kg

    return frete

def main():
    try:
        distancia = float(input("Informe a distância da entrega em km: "))
        peso = float(input("Informe o peso do pacote em kg: "))
        valor_frete = calcular_frete(distancia, peso)
        print(f"O valor do frete é: R${valor_frete:.2f}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos para distância e peso.")

if __name__ == "__main__":
    main()