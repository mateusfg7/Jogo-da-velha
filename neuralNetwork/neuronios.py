def sinapse_um(valorUm, valorDois, valorTres, pesos):
    
    values = [[],[]]

    values[0] = [valorUm*pesos[0], valorDois*pesos[1], valorTres*pesos[2]]
    values[1] = [valorUm*pesos[3], valorDois*pesos[4], valorTres*pesos[5]]

    soma = []
    for index in range(2):
        somatoria = 0
        for valor in values[index]:
            somatoria += valor
        if somatoria < 0:
            somatoria = 0
        soma.append(somatoria)
    return soma

def sinapse_dois(valorUm, valorDois, pesos):
    
    values = [[],[]]

    values[0] = [valorUm*pesos[6], valorDois*pesos[7]]
    values[1] = [valorUm*pesos[8], valorDois*pesos[9]]

    soma = []
    for index in range(2):
        somatoria = 0
        for valor in values[index]:
            somatoria += valor
        if somatoria < 0:
            somatoria = 0
        soma.append(somatoria)
    return soma