def floatEquals(f1, f2, tol = 0.000000001):
    return abs(f1-f2) <= tol
   
class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
       
       
    def semelhantes(self, t2):
        sides1 = sorted([self.a, self.b, self.c])
        sides2 = sorted([t2.a, t2.b, t2.c])
        semelhantes = True
        ratio = None
        for i in range(0, len(sides1)):
            newRatio = sides1[i]/sides2[i]
            if ratio != None and not floatEquals(newRatio, ratio):
                semelhantes = False
                break
            ratio = newRatio
            return semelhantes
       
       
t1 = Triangulo(3,4,5)
t2 = Triangulo(8,6,10)
print(t1.semelhantes(t2)) # True

t1 = Triangulo(3,4,5)
t2 = Triangulo(8,6,11)
print(t1.semelhantes(t2)) # False
