def verifica_aposentadoria():
    genero = input("Informe seu gênero ('M' para masculino ou 'F' para feminino): ").strip().upper()
    idade = int(input("Informe sua idade: "))
    tempo_servico = int(input("Informe seu tempo de serviço (em anos): "))

    if (genero == 'F' and (idade > 60 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25))) or \
       (genero == 'M' and (idade > 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25))):
        print(True)
    else:
        print(False)

verifica_aposentadoria()