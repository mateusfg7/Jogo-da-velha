import os


def render(player, casas):

    os.system('clear')

    print(f"\033[00;37mPlayer Atual: \033[00;31m{player}\033[00;37m\n")

    print(
        f"\033[00;31m{casas['1']} \033[00;37m| \033[00;31m{casas['2']} \033[00;37m| \033[00;31m{casas['3']}")
    print(f"\033[00;37m---------")
    print(
        f"\033[00;31m{casas['4']} \033[00;37m| \033[00;31m{casas['5']} \033[00;37m| \033[00;31m{casas['6']}")
    print(f"\033[00;37m---------")
    print(
        f"\033[00;31m{casas['7']} \033[00;37m| \033[00;31m{casas['8']} \033[00;37m| \033[00;31m{casas['9']}")
