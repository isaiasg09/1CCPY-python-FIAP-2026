# sistema que recolhe escolha do usuario
# escolha_usuario
# 0 = sair do programa
# 1 = entrar no programa
# ----- erro

escolha = 3
match escolha:
    case 0:
        print("Sair")
    case 1:
        print("Entrar")

    case _: # o else
        print("erro")

