def semelhantes(triangulo):
        set1 = set(triangulo.__dict__.values())
        set2 = set(self.__dict__.values())
        return set1 == set2

class Triangulo(object):

    def __eq__(self, triangulo):
        set1 = set(triangulo.__dict__.values())
        set2 = set(self.__dict__.values())
        return set1 == set2


t1 = Triangulo()
t1.a = 1
t1.b = 2
t1.c = 3

t2 = Triangulo()
t2.a = 1
t2.b = 3
t2.c = 3

print (t1 == t2)
