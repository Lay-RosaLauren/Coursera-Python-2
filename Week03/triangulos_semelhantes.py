class Triangulo:
    
    def __init__(self, a, b, c):
        self.lados = sorted([a, b, c])

    def semelhantes(self, Triangulo):
        x = Triangulo.lados
        if x[0] >= self.lados[0] and x[1] >= self.lados[1] and x[2] >= self.lados[2]:
            if x[0] % self.lados[0] == 0 and x[1] % self.lados[1] == 0 and x[2] % self.lados[2] == 0:
                return True
            else:
                return False
        if x[0] <= self.lados[0] and x[1] <= self.lados[1] and x[2] <= self.lados[2]:
            if self.lados[0] % x[0] == 0 and self.lados[1] % x[1] == 0 and self.lados[2] % x[2] == 0:
                return True
            else:
                return False
