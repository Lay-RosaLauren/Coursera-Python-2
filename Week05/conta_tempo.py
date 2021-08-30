import ordenador
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista
    
    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordenador()
        
        print('Comparando com listas aleatorias') 
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print('Bolha curta demorou ', depois - antes)
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Selecao direta demorou ', depois - antes)

        print('\nComparando com listas quase ordenadas')
        
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print('Bolha curta demorou ', depois - antes)
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print('Selecao direta demorou ', depois - antes)
