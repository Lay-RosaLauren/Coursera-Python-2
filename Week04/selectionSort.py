def ordena(list: list) -> list:
    '''Recebe uma lista e retorna a mesma ordenada crescentemente.'''
    n_list = list[:]

    for i in range(len(n_list)-1):
        min_position = i

        for j in range(i+1, len(n_list)):
            if n_list[j] < n_list[min_position]:
                min_position = j

        n_list[i], n_list[min_position] = n_list[min_position], n_list[i]

    return n_list
