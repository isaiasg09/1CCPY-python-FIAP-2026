# exibir todas as duplas possiveis numa lista de nomes
nomes=["joao","ale","bia","jo"]


for i in range(len(nomes)) :
    for j in range(len(nomes)): # o professor fez começando a iteração aq no j com i+1
        # da pra escrever tb o if sendo j>i, fznd com q só itere no j os itens à frente do i
        # garante que os nomes que já foram iterados no loop do i não passem
        if(i<j) :
            print(nomes[i], nomes[j])
