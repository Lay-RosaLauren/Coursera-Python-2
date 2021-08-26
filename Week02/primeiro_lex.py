def primeiro_lex(lista):
    # se não receber uma lista valida, retorne False
    if not len(lista) or type(lista) != list:
        return False

    # define a variável com o valor do primeiro elemento da lista recebida
    primeiro_string = lista[0]

    for s in lista:
        # realiza a comparação de ordem lexicográfica
        if s < primeiro_string:
            primeiro_string = s

    return primeiro_string

# Testa a ordem lexicográfica (letras maiúsculas e minúsculas)
def test_ordem_lexicografica():
    lista = ['oĺá', 'A', 'a', 'casa']
    assert primeiro_lex(lista) == "A"

# Testa lista vazia
def test_lista_vazia():
	lista = []
	assert primeiro_lex(lista) == False

# Testa lista inválida
def test_lista_invalida():
	lista = "maça banana laranja"
	assert primeiro_lex(lista) == False
