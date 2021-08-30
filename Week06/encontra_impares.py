def encontra_impares(lista):
    
    if len(lista) == 0:
        return []
    if lista[0] % 2 != 0: # para elemento impar
        return [lista[0]] + encontra_impares(lista[1:])
    else:
        return encontra_impares(lista[1:])
