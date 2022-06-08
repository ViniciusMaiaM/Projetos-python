from random import randint
qjog = input('Quer jogar (S/N)? ')
while qjog.upper() == 'S':
    velha = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    print("Tabuleiro")

    for i in range(3):
        for j in range(3):
            print(velha[i][j], end=' ')
        print()

    joga = 0
    ganhou = False
    jogganha = False
    pcganha = False
    deuvelha = False

    while joga <= 9 and not (ganhou):

        invalidax = False

        while not(invalidax):

            print("Vez do Jogador X")
            i = int(input("Informe a linha: "))
            j = int(input("Informe a coluna: "))

            if i > 3 or j > 3:

                print("jogada invalida, jogue novamente!")

            else:

                qc = velha[i-1][j-1]

                if qc == "0" or qc == "X":

                    print("jogada invalida, jogue novamente!")

                else:

                    velha[i-1][j-1] = 'X'

                    for i in range(3):
                        for j in range(3):
                            print(velha[i][j], end=' ')
                        print()
                    joga += 1
                    invalidax = True

        invalidao = False

        if joga == 9:
            ganhou = True
            deuvelha = True
            invalidao = True

        while not(invalidao):

            print("Vez do Jogador 0")
            i = randint(1, 3)
            j = randint(1, 3)
            cq = velha[i-1][j-1]

            if cq == "X" or cq == "0":
                print()

            else:
                velha[i-1][j-1] = '0'
                for i in range(3):
                    for j in range(3):
                        print(velha[i][j], end=' ')
                    print()
                joga += 1
                invalidao = True

        if (velha[0][0] == velha[0][1]) and (velha[0][1] == velha[0][2]) and (velha[0][2] == 'X'):
            ganhou = True
            jogganha = True
        elif (velha[1][0] == velha[1][1]) and (velha[1][1] == velha[1][2]) and (velha[1][2] == 'X'):
            ganhou = True
            jogganha = True
        elif (velha[2][0] == velha[2][1]) and (velha[2][1] == velha[2][2]) and (velha[2][2] == 'X'):
            ganhou = True
            jogganha = True
        elif (velha[0][0] == velha[1][0]) and (velha[1][0] == velha[2][0]) and (velha[2][0] == 'X'):
            ganhou = True
            jogganha = True
        elif (velha[0][1] == velha[1][1]) and (velha[1][1] == velha[2][1]) and (velha[2][1] == 'X'):
            ganhou = True
            jogganha = True
        elif (velha[0][2] == velha[1][2]) and (velha[1][2] == velha[2][2]) and (velha[2][2] == 'X'):
            ganhou = True
            jogganha = True
        elif (velha[0][0] == velha[1][1]) and (velha[1][1] == velha[2][2]) and (velha[2][2] == 'X'):
            ganhou = True
            jogganha = True
        elif (velha[0][2] == velha[1][1]) and (velha[1][1] == velha[2][0]) and (velha[2][0] == 'X'):
            ganhou = True
            jogganha = True

        elif (velha[0][0] == velha[0][1]) and (velha[0][1] == velha[0][2]) and (velha[0][2] == '0'):
            ganhou = True
            pcganha = True
        elif (velha[1][0] == velha[1][1]) and (velha[1][1] == velha[1][2]) and (velha[1][2] == '0'):
            ganhou = True
            pcganha = True
        elif (velha[2][0] == velha[2][1]) and (velha[2][1] == velha[2][2]) and (velha[2][2] == '0'):
            ganhou = True
            pcganha = True
        elif (velha[0][0] == velha[1][0]) and (velha[1][0] == velha[2][0]) and (velha[2][0] == '0'):
            ganhou = True
            pcganha = True
        elif (velha[0][1] == velha[1][1]) and (velha[1][1] == velha[2][1]) and (velha[2][1] == '0'):
            ganhou = True
            pcganha = True
        elif (velha[0][2] == velha[1][2]) and (velha[1][2] == velha[2][2]) and (velha[2][2] == '0'):
            ganhou = True
            pcganha = True
        elif (velha[0][0] == velha[1][1]) and (velha[1][1] == velha[2][2]) and (velha[2][2] == '0'):
            ganhou = True
            pcganha = True
        elif (velha[0][2] == velha[1][1]) and (velha[1][1] == velha[2][0]) and (velha[2][0] == '0'):
            ganhou = True
            pcganha = True

    if jogganha == True:
        print("Jogador Venceu")

    elif pcganha == True:
        print("Computador Venceu")

    elif deuvelha == True:
        print('Deu velha Porra!')

    qjog = input('Quer jogar novamente (S/N)? ')
