# Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1,
# o número de peças1 que o usuário quer, o valor unitário de cada peça1,
# o nome de uma peça2, o número de peças2 e o valor unitário de cada peça2.
# Depois, calcule e mostre o valor a ser pago.

nome_peca1 = input("Digite o nome da peça 1: ")
num_peca1 = int(input("Digite o numero de peças 1 que você quer: "))
valor_peca1 = float(input("Digite o valor da peça 1: "))

nome_peca2 = input("Digite o nome da peça 2: ")
num_peca2 = int(input("Digite o numero de peças 2 que você quer: "))
valor_peca2 = float(input("Digite o valor da peça 2: "))

total = (num_peca1*valor_peca1) + (num_peca2*valor_peca2)

print(f"O total a ser pago é de {total} reais.")
