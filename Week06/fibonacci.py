def fibonacci(n):
    if n < 2:       #base da recursao
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)   #chamada recursiva

import pytest

@pytest.mark.parametrize('entrada, esperado', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    ])
def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado
    
