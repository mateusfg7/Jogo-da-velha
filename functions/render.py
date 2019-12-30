import os

from functions.colors import cor
cor = cor()

def render(player, casas):
    
    os.system('clear')
    
    print(f"{cor['white']}Player Atual: {cor['red']}{player}{cor['white']}\n")

    print(f"{cor['red']}{casas['1']} {cor['white']}| {cor['red']}{casas['2']} {cor['white']}| {cor['red']}{casas['3']}")
    print(f"{cor['white']}---------")
    print(f"{cor['red']}{casas['4']} {cor['white']}| {cor['red']}{casas['5']} {cor['white']}| {cor['red']}{casas['6']}")
    print(f"{cor['white']}---------")
    print(f"{cor['red']}{casas['7']} {cor['white']}| {cor['red']}{casas['8']} {cor['white']}| {cor['red']}{casas['9']}")