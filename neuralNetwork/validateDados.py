import pandas

def validateDados(valorUm, valorDois, valorTres):
    csv = 'neuralNetwork/learned.csv'
    learnedDados = pandas.read_csv(csv)
    
    inputDados = f'{valorUm},{valorDois},{valorTres}'

    index = 0
    while index < len(learnedDados):
        currenctDados = f'{learnedDados["valorUm"][index]},{learnedDados["valorDois"][index]},{learnedDados["valorTres"][index]}'
        if inputDados == currenctDados:
            return learnedDados['resultado'][index]
        index += 1
    else:
        return False