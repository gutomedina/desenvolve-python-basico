def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return "Bissexto"
    else:
        return "Não Bissexto"

anos_para_testar = [1900, 2000, 2016, 2017]
for ano in anos_para_testar:
    print(f"Ano {ano}: {verificar_ano_bissexto(ano)}")

# Solicitar ao usuário para inserir um ano
ano_usuario = int(input("Insira um ano para verificar se é bissexto: "))
print(verificar_ano_bissexto(ano_usuario))