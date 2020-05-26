def drawCondition(positions):
    markedPositions = 0
    index = 1
    while index <= len(positions):
        if positions[str(index)] == 'X' or positions[str(index)] == 'O':
            markedPositions += 1
        index += 1
    if markedPositions == 9:
        print(f"\033[00;37mO jogo deu \033[00;31mempate\033[00;37m!")
        exit()
    else:
        return False


def winCondition(one, two, three, position, player1, player2):
    if position[one] == player1 and position[two] == player1 and position[three] == player1:
        print(
            f"\n\033[00;37mParabens \033[00;31m{player1} \033[00;37mvocê ganhou!")
        exit()
    if position[one] == player2 and position[two] == player2 and position[three] == player2:
        print(
            f"\n\033[00;37mParabens \033[00;31m{player2} \033[00;37mvocê ganhou!")
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
    return True
