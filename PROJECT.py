AGENDA = {}

AGENDA['Guilherme'] = {
    'telefone': '992991387',
    'e-mail': 'guilherme@solyd.com.br',
    'endereço': 'Av. 1',
}

AGENDA['Maria'] = {
    'telefone': '992991432',
    'e-mail': 'maria@solyd.com.br',
    'endereço': 'Av. 2',
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print('--------------------------------------')



def buscar_contato(contato):
    print('Nome:', contato)
    print("Telefone:", AGENDA[contato]['telefone'])
    print("E-mail:", AGENDA[contato]['e-mail'])
    print("Endereço:", AGENDA[contato]['endereço'])
    print('--------------------------------------')


def incluir_contato(contato,telefone,email,endereço):
    AGENDA[contato] = {
        'telefone': telefone,
        'e-mail': email,
        'endereço': endereço,
    }
    print('>>>> contato {} adicionado com sucesso'.format(contato))


def excluir_contato(contato):
    AGENDA.pop(contato)
    print('>>>> contato {} excluído com sucesso'.format(contato))

def imprimir_menu():
    print('1 - Mostrar agenda inteira')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar agenda')



while True:
    imprimir_menu()

    opcao = input('Digite a opção: \n')
    print(opcao)
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        buscar_contato(input('Digite o nome do contato: \n',))
        if buscar_contato() == False:
            print('Contato não existente')
    elif opcao == '3':
        incluir_contato(input('Nome: \n', ), input('Telefone: \n',), input('E-mail: \n',), input('Endereço: \n',))
        mostrar_contatos()
    elif opcao == '4':
        incluir_contato(input('Nome: \n', ), input('Telefone: \n',), input('E-mail: \n',), input('Endereço: \n',))
    elif opcao == '5':
        excluir_contato(input('Digite o nome do contato: \n', ))
    elif opcao == '0':
        print('Programa fechado')
        break
    else:
        print('Opção inválida')







