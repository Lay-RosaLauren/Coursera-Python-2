def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com nu_linhas linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado.
    '''
    cria_matriz = [] # lista vazia
    for i in range(num_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)

        # adiciona linha à matriz
        cria_matriz.append(linha)

    return cria_matriz    
