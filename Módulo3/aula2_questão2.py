
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))


ambos_maior_de_idade = idade_juliana > 17 and idade_cris > 17
print(ambos_maior_de_idade)


pelo_menos_um_maior_de_idade = idade_juliana > 17 or idade_cris > 17
print(pelo_menos_um_maior_de_idade)