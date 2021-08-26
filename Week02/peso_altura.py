def peso_altura():
    return 44, 1.47

def pagamento_semanal (valor_por_hora, num_horas = 40):
    assert valor_por_hora >= 0 and num_horas > 0
    return valor_por_hora * num_horas
