class Triangulo:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def gerar_lados_ordenados(self):
        return sorted([self.a, self.b, self.c])

    def semelhantes(self, triangulo):
        lados_triangulo_1 = list(self.gerar_lados_ordenados())
        lados_triangulo_2 = list(triangulo.gerar_lados_ordenados())

    def __eq__(self, triangulo):
        lados_triangulo_1 = list(self.gerar_lados_ordenados())
        lados_triangulo_2 = list(triangulo.gerar_lados_ordenados())
        return lados_triangulo_1 == lados_triangulo_2
