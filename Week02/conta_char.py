def conta_letras(frase, contar="vogais"):
    vogais = consoantes = 0

    # mapa de vogais ASCII
    mapa_de_vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # remove os espaços em branco
    frase = frase.replace(" ", "")

    for i in range(len(frase)):
        caracter = frase[i]

        # verifica se o caracter é uma vogal e incrementa a variável respectiva
        # de acordo com o resultado
        if caracter in mapa_de_vogais:
            vogais += 1
        else:
            consoantes += 1

    # retorna a quantidade de vogais ou consoantes 
    # parâmetro contar
    return vogais if contar == 'vogais' else consoantes

# Testa a contagem de vogais
def test_conta_vogais():
    assert conta_letras('programamos em python') == 6

# Testa a contagem de consoantes
def test_conta_consoantes():
    assert conta_letras('programamos em python', 'consoantes') == 13
