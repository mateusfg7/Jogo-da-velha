from functions.colors import cor
cor = cor()

def winCondition(um, dois, tres, casa, player1, player2):
    if casa[um] == player1 and casa[dois] == player1 and casa[tres] == player1:
        print(f"\n{cor['white']}Parabens {cor['red']}{player1} {cor['white']}você ganhou!")
        exit()
    if casa[um] == player2 and casa[dois] == player2 and casa[tres] == player2:
        print(f"\n{cor['white']}Parabens {cor['red']}{player2} {cor['white']}você ganhou!")
        exit()