from os import remove


agenda = []
escolha = ""

while escolha != '0':
    print('=========================')
    print('==== Programa Agenda ====')
    print('=========================')
    print('= 1 - Cadastrar contato =')
    print('= 2 - Pesquisar contato =')
    print('= 3 - Atualizar contato =')
    print('= 4 - Apagar contato    =')
    print('= 5 - Listar todos      =')
    print('= 0 - Sair              =')
    print('=========================')
    escolha = input('Escolha sua opção: ')

    if escolha == '1':  # Adicionando contatos
        print()
        print('Módulo de cadastro:\n')

        contato = []
        nome = input('Insira o nome: ')
        contato.append(nome)
        nume = input('Insira o contato: ')
        contato.append(nume)
        email = input('Insira o email: ')
        contato.append(email)
        agenda.append(contato)  # Passando pra lista
        print()

    elif escolha == '2':  # Função de pesquisa
        print()
        print('Módulo de pesquisa: \n')
        nome_bus = input('Insira o nome que você quer procurar: ')
        achou = False
        for pessoa in agenda:
            # se o nome está nesta lista
            if nome_bus.upper() in pessoa[0].upper() and not achou:
                print()
                print('Nome:\t', pessoa[0])
                print('Número:\t', pessoa[1])
                print('Email:\t', pessoa[2])
                print()
                achou = True
        print()
        if not achou:
            print('Nome não encontrado')
        print()

    elif escolha == '3':  # Função para atualizar o contato
        print()
        print('Módulo de Atualização:\n')
        nome_bus = input('Nome a procurar: ')
        achou = False
        for pessoa in agenda:
            # Mesma estrutura do módulo de busca
            if nome_bus.upper() in pessoa[0].upper() and not achou:
                print()
                print('Contato atual:\n')
                print('Nome:\t', pessoa[0])
                print('Número:\t', pessoa[1])
                print('Email:\t', pessoa[2])
                print('\nAgora você aplicará as mudanças no contato \n')

                nome = input('Insira a mudança no nome: ')
                pessoa[0] = nome
                agenda.append(pessoa[0])
                nume = input('Insira a mudança no número: ')
                pessoa[1] = nume
                agenda.append(pessoa[1])
                email = input('Insira a mudança no email: ')
                pessoa[2] = email
                agenda.append(pessoa[2])

                print('\nAs mudanças foram aplicadas: ')
                print('Nome:\t', pessoa[0])
                print('Número:\t', pessoa[1])
                print('Email:\t', pessoa[2])
                print()
                achou = True

        if not achou:
            print('Nome não encontrado')
        print()

    elif escolha == '4':  # Função para excluir
        print()
        print('Módulo de Exclusão:\n')
        nome_bus = input('Nome a procurar: ')
        achou = False
        for excl in agenda:
            if nome_bus.upper() in excl[0].upper() and not achou:
                print()
                print('Contato para a exclusão:\n')
                print('Nome:\t', excl[0])
                print('Número:\t', excl[1])
                print('Email:\t', excl[2])
                achou = True
                ex = input('Quer excluir este contato(S/N)?')
                if ex.upper() == "S":
                    for excl in agenda:  # ainda tenho que buscar uma solução melhor
                        del agenda[0]

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
