# Converta uma temperatura de Fahrenheit para Celsius.
# A fórmula de conversão é: Celsius = (Fahrenheit -32) * 5/9

faren = float(input("Digite a temperatura em Farenheit: "))
celsius = (faren - 32)*(5/9)

print(f"A temperatura em Celsius é {celsius}")