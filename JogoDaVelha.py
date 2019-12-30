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

while True:
    print('\n')
    print(" 1 2 3")
    print(f"A{casas['A1']} {casas['A2']} {casas['A3']}")
    print(f"B{casas['B1']} {casas['B2']} {casas['B3']}")
    print(f"C{casas['C1']} {casas['C2']} {casas['C3']}")

    mark = input("-> ")
    casas[mark] = 'x'
