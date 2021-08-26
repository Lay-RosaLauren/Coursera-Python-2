def menor_nome(nomes):
	# se não receber uma lista de nomes valida, retorne "False"
	if not len(nomes) or type(nomes) != list:
		return "False"

	# inicia o nome curto com o primeiro nome da lista recebida
	menor_nome = nomes[0]
	comprimento_mais_curto = len(nomes[0])

	for nome in nomes:
		# quando houver espaços em branco, remova-os
		nome = nome.strip()

		# se encontrar um nome menor que o nome definido como mais curto,
		# substitua-o
		if len(nome) < comprimento_mais_curto:
			comprimento_mais_curto = len(nome)
			menor_nome = nome

	# retorne o nome mais curto capitalizado
	return menor_nome.capitalize()


# Testa o nome mais curto
def test_menor_nome():
	nomes = [    'ana', 'josé',     'Arquibaldo',     'Alouhis']
	assert menor_nome(nomes) == 'ana'

# Testa nomes com espaços em branco
def test_nomes_com_espacos():
	nomes = [    'ana', ' josé  ', '  Arquibaldo',     'Alouhis  ']
	assert menor_nome(nomes) == 'ana'

# Testa nomes com letras maiúsculas e minúsculas
def test_nomes_maiusculas_minusculas():
	nomes = ['Carolina', 'JOSÉ  ', 'Bin']
	assert menor_nome(nomes) == 'Bin'

# Testa nomes com mesmo comprimento
def test_nomes_mesmo_comprimento():
	nomes = ['bi', ' ro', 'mi']
	assert menor_nome(nomes) == 'bi'

# Testa lista de nomes vazia
def test_lista_de_nomes_vazia():
	nomes = []
	assert menor_nome(nomes) == 'False'

# Testa lista inválida
def test_lista_de_nomes_invalida():
	nomes = 'beatriz'
	assert menor_nome(nomes) == 'False'
