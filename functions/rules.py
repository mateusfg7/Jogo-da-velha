from functions.colors import cor
cor = cor()

def drawCondition(positions):
    markedPositions = 0
    index = 1
    while index <= len(positions):
        if positions[str(index)] == 'X' or positions[str(index)] == 'O':
            markedPositions += 1
        index += 1
    if markedPositions == 9:
        print(f"{cor['white']}O jogo deu {cor['red']}empate{cor['white']}!")
        exit()
    else:
        return False

def winCondition(one, two, three, position, player1, player2):
    if position[one] == player1 and position[two] == player1 and position[three] == player1:
        print(f"\n{cor['white']}Parabens {cor['red']}{player1} {cor['white']}você ganhou!")
        exit()
    if position[one] == player2 and position[two] == player2 and position[three] == player2:
        print(f"\n{cor['white']}Parabens {cor['red']}{player2} {cor['white']}você ganhou!")
        exit()

def winCases():
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

    return casosDeVitorias

def validateChoice(player, choice, position):
    if position[choice] == 'X' or position[choice] == 'O':
        return False
    else:
        return True