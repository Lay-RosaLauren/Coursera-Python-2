def dimensoes(matriz):
    return (len(matriz), len(matriz[0]))

# Verifica se as matrizes recebidas são multiplicavéis
def sao_multiplicaveis(m1, m2):
    dimensao_m1 = dimensoes(m1)
    dimensao_m2 = dimensoes(m2)

    if dimensao_m1[1] == dimensao_m2[0]:
        return True
    else:
        return False
