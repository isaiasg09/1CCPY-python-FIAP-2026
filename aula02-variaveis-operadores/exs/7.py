# Leia 2 valores A e B, que correspondem a 2 notas de um aluno.
# A seguir calcule e informe a média ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.
# Exemplo: nota a * 4 e nota b * 6.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = ((n1*4)+(n2*6))/2

print(f"A média do aluno foi {media}")