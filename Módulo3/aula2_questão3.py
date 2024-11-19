idade = int(input("Digite sua idade: "))
jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? ").strip().lower() == 'true'
quantidade_vitorias = int(input("Quantos jogos já venceu? "))

apto_para_ingressar = (16 <= idade <= 18) and jogou_tres_jogos and (quantidade_vitorias >= 1)

print("Apto para ingressar no clube de jogos de tabuleiro:", apto_para_ingressar)