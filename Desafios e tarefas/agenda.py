agenda = []
escolha = ""

while escolha != '0':
    print('=========================')
    print('==== Programa Agenda ====')
    print('=========================')
    print('  1 - Cadastrar contato  ')
    print('  2 - Pesquisar contato  ')
    print('  3 - Atualizar contato  ')
    print('  4 - Apagar contato     ')
    print('  5 - Listar todos       ')
    print('  0 - Sair               ')
    escolha = input('Escolha sua opção: ')

    if escolha == '1':
        print()
        print('Módulo de cadastro:\n')

        contato = []
        nome = input('Insira o nome: ')
        contato.append(nome)
        nume = input('Insira o contato: ')
        contato.append(nume)
        email = input('Insira o email: ')
        contato.append(email)
        agenda.append(contato)
        print()

    elif escolha == '2':
        print()
        print('Módulo de pesquisa\n')
        nome_bus = input('Insira o nome que você quer procurar: ')
        for pessoa in agenda:
            if nome_bus.upper() in pessoa[0].upper():
                print()
                print('Nome:\t', pessoa[0])
                print('Número:\t', pessoa[1])
                print('Email:\t', pessoa[2])
                print()
        print()

    elif escolha == '3':
        print()
        print('Módulo de exclusão')
        nome_bus = input('Nome a procurar: ')
        achou = False
        for pessoa in agenda:
            if nome_bus.upper() in pessoa[0].upper():
                achou = True
                print()
                print('Nome:\t', pessoa[0])
                print('Número:\t', pessoa[1])
                print('Email:\t', pessoa[2])
                print()
        if not achou:
            print('Nome não encontrado')
        print()

    elif escolha == '5':
        print()
        print('Módulo de listagem\n')
        for i in agenda:
            print('Nome:\t', i[0])
            print('Número:\t', i[1])
            print('Email:\t', i[2])
            print()
        print()

    elif escolha == '0':
        print()
        print('Módulo de encerramento\n')
        print()
