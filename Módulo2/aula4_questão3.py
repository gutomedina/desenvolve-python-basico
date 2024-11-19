def obter_dados_do_produto(numero_produto):
    nome = input(f"Digite o nome do produto {numero_produto}: ")
    preco_unitario = float(input(f"Digite o preço unitário do produto {numero_produto}: "))
    quantidade = int(input(f"Digite a quantidade do produto {numero_produto}: "))
    return preco_unitario, quantidade

def calcular_preco_total(preco_quantidade):
    total = 0
    for preco, quantidade in preco_quantidade:
        total += preco * quantidade
    return total

def main():
    preco_quantidade = []
    for i in range(1, 4):
        preco, quantidade = obter_dados_do_produto(i)
        preco_quantidade.append((preco, quantidade))
        
    total = calcular_preco_total(preco_quantidade)
    
    print(f"Total: R${total:,.2f}")

if __name__ == "__main__":
    main()