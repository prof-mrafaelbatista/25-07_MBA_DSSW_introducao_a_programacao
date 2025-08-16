def cadastrar_sh(num_sh):
    """
    Cadastra um número especificado de super-heróis.

    Args:
        num_sh (int): O número de super-heróis a serem cadastrados.
    """
    for i in range(num_sh):
        nome = input('Digite o nome do Super Hero: ')
        skill = input('Digite a skill do Super Hero: ')
        lista_sh.append([nome, skill])
        print(f'O sh {nome} foi cadastrado com sucesso!')


def listar_sh(lista):
    tam_sh = len(lista)
    for i in range(tam_sh):
        print(f'[{i}] - {lista[i][0]} - {lista[i][1]}')

lista_sh = [['Hulk', 'Super força'], ['Batman', 'Rico']]

while True:
    print('#### SISTEMA DE SUPER HERO ####')
    print('1 - Cadastrar um super hero')
    print('2 - Alterar um super hero')
    print('3 - Deletar um super hero')
    print('4 - Listar os super heros')
    print('0 - Sair do sistema')

    op = int(input('Digite a opção desejada: '))

    if op == 1:
        print('#### CADASTRO DE SUPER HEROS ####')
        n_sh = int(input('Deseja cadastrar quantos SH?'))
        if 0 < n_sh < 11:
            cadastrar_sh(n_sh)
        else:
            print('Esse número de SH é inválido!')


    elif op == 2:
        print('#### ALTERAR UM SUPER HEROS ####')
        listar_sh(lista_sh)
        op_alt = int(input('Digite o herói a ser alterado: '))
        nome = input('Digite o nome do Super Hero: ')
        skill = input('Digite a skill do Super Hero: ')
        lista_sh[op_alt] = [nome, skill]


    elif op == 3:
        print('#### DELETAR UM SUPER HEROS ####')

        listar_sh(lista_sh)
        op_del = int(input('Digite o herói a ser deletado: '))
        del lista_sh[op_del]

    elif op == 4:
        print('#### LISTA DE SUPER HEROS ####')
        listar_sh(lista_sh)

    elif op == 0:
        print('Saindo do sistema')
        break
    else:
        print('Digite uma opção válida!')