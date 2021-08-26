def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s
print(horario_em_segundos (-1,20,30))
