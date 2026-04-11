# RELACIONAIS
idade=20
maior_idade = idade>=18

if maior_idade:
    print("Maior de idade")

# OPERADORES LOGICOS
# AND, OR, NOT

verifica_email=True
verifical_senha=True

login = verifica_email and verifical_senha

print(login)

if not login:
    print("C é burro, tenta dnv")


# NOTAS...
print() # pular linha
nota_final=6

if nota_final<4:
    print("reprovado")
elif nota_final<6:
        print("recuperação")
else:
    print("aprovado")

print("fim")