def linha(tam=42):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def tirar_extrato(saldo, /, *, extrato):
    if not extrato:
        print('Nenhum movimentação foi realizada')
    else:
        print(extrato)
        print(f'Saldo: R$ {saldo:.2f}\n')


def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    limite_saldo = saque > saldo
    limite_saque = numero_saques >= limite_saques
    saque_excedido = saque > limite

    if limite_saldo:
        print('Operação falhou! Saldo insuficiente.')
    elif saque_excedido:
        print('Operação falhou! Valor excede o limite de saque por vez')
    elif limite_saque:
        print('Operação falhou! Limite diario de saque excedido')

    elif saque > 0:
        print(f'Saque de {saque:.2f} realizado com sucesso!')
        saldo -= saque
        extrato += f'Saque: R${saque:.2f}\n'
        numero_saques += 1
    else:
        print('Operação falhou! Informe um valor válido.')

    return saldo, extrato


def depositar(deposito, saldo, extrato, /):
    if deposito > 0:
        print(f'Depósito de R${deposito:.2f} realizado com sucesso')
        saldo += deposito
        extrato += f'Depósito: R${deposito:.2f}\n'
    else:
        print('Informe um valor válido para depósito!')
    return saldo, extrato


def menu(lista):
    cabecalho('OPERAÇÕES BANCO')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opcao = int(input('Escolha uma opcao: '))
    return opcao


def cadastrar_cliente(clientes):
    cabecalho('Cadastro')
    cpf = input('Informe o CPF (apenas números): ')
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print('Já existe esse cadastro com esse CPF')
        return
    nome = input('Digite o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: (logradouro, nro-bairro- cidade/estado-sigla): ')
    clientes.append({'nome': nome, 'data de nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    cabecalho('Usuario criado com sucesso')


def filtrar_cliente(cpf, usuarios):
    filtro_usuarios = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return filtro_usuarios[0] if filtro_usuarios else None


def cadastrar_conta(agencia, numero_conta, cliente):
    cpf = input('Informe o cpf do cliente: ')
    cliente = filtrar_cliente(cpf, cliente)

    if cliente:
        cabecalho('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'cliente': cliente}
    print('Cliente não encontrado, cadastro encerrado!')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        cabecalho('')
        print(linha)


def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    numero_saques = 0
    extrato = ''
    clientes = []
    contas = []
    while True:
        resposta = menu(
            ['Depositar', 'Sacar', 'Extrato', 'Cadastrar conta', 'Cadastrar cliente', 'listar contas', 'Sair'])
        if resposta == 1:
            cabecalho('DEPÓSITO')
            deposito = float(input('Valor que deseja depositar: '))
            saldo, extrato = depositar(deposito, saldo, extrato)
        elif resposta == 2:
            cabecalho('SAQUE')
            saque = float(input('Valor do saque: '))
            saldo, extrato = sacar(saldo=saldo, saque=saque, extrato=extrato, limite=limite,
                                   numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif resposta == 3:
            cabecalho('EXTRATO')
            tirar_extrato(saldo, extrato=extrato)
        elif resposta == 4:
            numero_conta = len(contas)+1
            conta = cadastrar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)
        elif resposta == 5:
            cadastrar_cliente(clientes)
        elif resposta == 6:
            listar_contas(contas)
        elif resposta == 7:
            cabecalho('\033[0;31mEncerrando o sistema!\033[m')
            break
        else:
            print('Operação inválida! Escolha uma operação válida.')


main()