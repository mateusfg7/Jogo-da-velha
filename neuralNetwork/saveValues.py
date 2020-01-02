def salvarDados(valor1,valor2,valor3,resultado):
    with open('neuralNetwork/learned.csv', 'a') as arquivo:
        arquivo.writelines(f'\n{valor1},{valor2},{valor3},{resultado}')