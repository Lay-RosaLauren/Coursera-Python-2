def ordenada(list: list) -> bool:
    """Verifica se uma lista esta ordenada."""
    if not list:
        return False

    ordered_list = sorted(list)
    return True if ordered_list == list else False
