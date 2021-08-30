class Triangulo(object):

    def __init__(self, a, b, c):
        self.lados = sorted([a, b, c])

    def semelhante(self, outro):
        r = sum(self.lados) / sum(outro.lados)
        return all(k / z == r for k, z in zip(self.lados, outro.lados))

if __name__ == '__main__':
    a = Triangulo(2, 4, 6)
    b = Triangulo(4, 8, 12)
    c = Triangulo(12, 8, 4)

    print("%s semelhante %s: %r" % ('a', 'b', a.semelhante(b)))
    print("%s semelhante %s: %r" % ('a', 'c', a.semelhante(c)))
    print("%s semelhante %s: %r" % ('b', 'c', b.semelhante(c)))
