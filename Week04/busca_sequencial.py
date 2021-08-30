def busca(list: list, element):
    """Verifica se um elemento esta na lista."""
    for i, el in enumerate(list):
        if element == el:
            return i

    return False
