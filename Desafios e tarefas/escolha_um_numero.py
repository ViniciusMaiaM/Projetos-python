from random import randint
jogar = input('Quer jogar (S/N)? ')
cont = 1  # contador
min = 1  # valor mínimo
max = 100  # valor maximo

while jogar.upper() == 'S':  # laço
    pc = randint(1, 100)
    print(pc)
    print()
    pes = int(input('Qual o seu número? '))

    while pes != pc and cont < 10:  # enquanto a o palpite for diferente do computador e a contagem for menor do que 10
        cont += 1

        if pes > pc:  # se o palpite do jogador for menor que o pc
            print()
            print('DIGITE UM NÚMERO MENOR')
            max = pes  # o valor maximo passa a ser o palpite do jogador
            print()
            pes = int(input('Qual sua outra tentativa? '))

            if pes >= max:  # se o jogador der um palpite maior que o maximo, então desclassificado
                print("Desclassificado por inserir um valor invalido")
                break

        else:
            print()
            print('DIGITE UM NÚMERO MAIOR')
            min = pes  # o valor minimo passa a ser o palpite do jogador
            print()
            pes = int(input('Qual sua outra tentativa? '))

            if pes <= min:  # se o jogador der um palpite menor que o minimo, então desclassificado
                print('Desclassificado por inserir um valor invalido')
                break

    if pes == pc and cont == 1:
        print('----------------------------')
        print('VOCÊ TEVE MUITA SORTE')

    elif pes == pc and cont >= 2 and cont <= 4:
        print('----------------------------')
        print('VOCÊ JOGA BEM, MAS AINDA CONTOU COM A SORTE')

    elif pes == pc and cont >= 5 and cont <= 7:
        print('----------------------------')
        print('VOCÊ É UM EXCELENTE ESTRATEGISTA')

    else:
        print('----------------------------')
        print('ANALISE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE')
    print('----------------------------')
    print('Você precisou de %d palpites' % cont)
    jogar = input('Quer jogar novamente? ')
    cont = 1
