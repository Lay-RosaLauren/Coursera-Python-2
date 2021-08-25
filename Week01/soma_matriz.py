
def dimensoes(matriz):
    return (len(matriz), len(matriz[0]))

def soma_matrizes(m1, m2):
    # calcula as dimensões das matrizes recebidas
    dimensao_m1 = dimensoes(m1)
    dimensao_m2 = dimensoes(m2)

    # Verifica se ambas possuem as mesmas dimensões
    if dimensao_m1 == dimensao_m2:
        matriz_soma = []

        # percorre as linhas
        for i in range(len(m1)):
            linha = []

            # percorre as colunas
            for j in range(len(m1[0])):

                # soma as matrizes e atribui os valores na linha
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)

            # inclui a linha resultante à nova matriz
            matriz_soma.append(linha)

        return matriz_soma
    else:
        return False
