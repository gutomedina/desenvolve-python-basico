def main():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        soma = num1 + num2
        
        if soma % 2 == 0:
            print("A soma dos números é par.")
        else:
            print("A soma dos números é ímpar.")
    
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    main()