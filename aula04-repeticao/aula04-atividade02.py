def validaNota(nota) :
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a primeira nota: "))

    return nota


nota1 = validaNota(float(input("Digite a primeira nota: ")))

nota2=validaNota(float(input("Digite a segunda nota: ")))

media=(nota1+nota2)/2

print(media)