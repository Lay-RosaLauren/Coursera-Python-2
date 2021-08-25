def ImprimirMatriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna, end="\t")
        print("")
