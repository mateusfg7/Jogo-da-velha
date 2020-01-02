from random import randrange

def calcularPesos():
    pesos = []
    index = 1
    while index <= 10:
        pesos.append(randrange(-1000, 1000))
        index += 1
    return pesos