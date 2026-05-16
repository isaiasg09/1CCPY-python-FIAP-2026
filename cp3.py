# Uma escola está testando um sistema simples de monitoramento ambiental para identificar salas com possível risco de calor excessivo.
# Você recebeu uma matriz em que cada linha representa uma sala e cada coluna representa a temperatura registrada em um horário diferente do dia.
# Programa vai calcular a média de cada sala e quantas vezes cada sala registrou temp >= 33

temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]


for i in range(len(temperaturas)) :
    # media e criticos resetam a cada sala
    media=0
    criticos=0
    sala = temperaturas[i] # pra loopar mais facil no segundo loop
    print(f"Sala {i+1}") # printa o numero da sala usando o indice do loop

    for registro in sala :
        media+=registro # adiciona cada temperatura registrada pra media, que sera dividida por 4 depois
        # se a temp registrada for crítica aumenta o número de críticos
        if(registro>=33) :
            criticos+=1

    media = media / len(sala) # divide a media pelo tamanho da array da sala atual

    print(f"Média: {media}")

    print(f"Registros críticos: {criticos}")

    print() # espaço vazio pra separar cada sala

