# Crie um programa que receba o valor do produto e valor pago.
# Calcule o troco a ser pago.
# O valor do troco deve ser exibido no terminal.

vprod = float(input("Digite o valor do produto: "))
vpag = float(input("Digite o valor pago: "))

troco = vpag - vprod

if troco<0 :
    print(f"Faltam {troco*(-1)} reais a serem pagos")
elif troco==0 :
    print("Não há troco")
else :
    print(f"O troco a ser pago é de {troco} reais")