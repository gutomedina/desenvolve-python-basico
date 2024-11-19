def fahrenheit_to_celsius(fahrenheit):
    celsius = int((fahrenheit - 32) * (5 / 9))
    return celsius

def main():
    fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")

if __name__ == "__main__":
    main()