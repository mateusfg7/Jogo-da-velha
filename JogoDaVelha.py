from functions.rules import winCondition
from functions.render import render

cor = {
    'red' : '\033[00;31m',
    'white' : '\033[00;37m'
}

casosDeVitorias = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7'],
]

casas = {
    '1' : '\033[00;37m1',
    '2' : '\033[00;37m2',
    '3' : '\033[00;37m3',
    '4' : '\033[00;37m4',
    '5' : '\033[00;37m5',
    '6' : '\033[00;37m6',
    '7' : '\033[00;37m7',
    '8' : '\033[00;37m8',
    '9' : '\033[00;37m9',
}

state = []

player = 'X'

while True:
    render(player, casas)
    
    for c in casosDeVitorias:
        winCondition(c[0], c[1], c[2], casas, 'X', 'O')

    mark = input("\n-> ")
    casas[mark] = player
    state.append(mark)

    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    
