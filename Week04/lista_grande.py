import random

def lista_grande(size: int) -> list:
    '''Recebe um número e devolve uma lista de elementos aleatórios.'''
    list = []

    for x in range(size):
        list.append(random.randint(1, 100))

    return list
