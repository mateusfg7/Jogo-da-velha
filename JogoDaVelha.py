from functions.rules import winCondition
from functions.rules import winCases
from functions.render import render
from functions.colors import cor

casosDeVitorias = winCases()

position = {
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

currenctPlayer = 'X'

while True:
    render(currenctPlayer, position)
    
    for c in casosDeVitorias:
        winCondition(c[0], c[1], c[2], position, 'X', 'O')

    choice = input("\n-> ")
    position[choice] = currenctPlayer

    if currenctPlayer == 'X':
        currenctPlayer = 'O'
    elif currenctPlayer == 'O':
        currenctPlayer = 'X'
    
