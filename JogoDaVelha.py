import os

def condição(um, dois, tres, casa, player1, player2):
    if casa[um] == player1 and casa[dois] == player1 and casa[tres] == player1:
        print(f'\nParabens {player1} você ganhou!')
        exit()
    if casa[um] == player2 and casa[dois] == player2 and casa[tres] == player2:
        print(f'\nParabens {player2} você ganhou!')
        exit()

casosDeVitorias = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3'],
    ['C1', 'C2', 'C3'],
    ['A1', 'B1', 'C1'],
    ['A2', 'B2', 'C2'],
    ['A3', 'B3', 'C3'],
    ['A1', 'B2', 'C3'],
    ['A3', 'B2', 'C1'],
]

casas = {
    'A1' : ' ',
    'A2' : ' ',
    'A3' : ' ',
    'B1' : ' ',
    'B2' : ' ',
    'B3' : ' ',
    'C1' : ' ',
    'C2' : ' ',
    'C3' : ' ',
}

state = []

player = 'X'

while True:
    os.system('clear')
    print(f"{player}  1   2   3\n")
    print(f"A  {casas['A1']} | {casas['A2']} | {casas['A3']}")
    print("   ---------")
    print(f"B  {casas['B1']} | {casas['B2']} | {casas['B3']}")
    print("   ---------")
    print(f"C  {casas['C1']} | {casas['C2']} | {casas['C3']}")
    
    for c in casosDeVitorias:
        condição(c[0], c[1], c[2], casas, 'X', 'O')

    mark = input("\n-> ")
    casas[mark] = player
    state.append(mark)

    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    
