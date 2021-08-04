from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    """ADICIONEI CORES AO MENU"""
    print('\033[31m==============================\033[m')
    print('\033[31m============\033[m \033[36mATM\033[m \033[31m=============\033[m')
    print('\033[31m=========\033[m \033[36mPYTHON BANK\033[m \033[31m========\033[m')
    print('\033[31m=\033[m' * 30)

    print('\033[32mSelecione uma opção no Menu\033[m')
    print('\033[7m1\033[m - \033[32mCriar conta\033[m')
    print('\033[7m2\033[m - \033[32mEfetuar Saque\033[m')
    print('\033[7m3\033[m - \033[32mEfetuar Deposito\033[m')
    print('\033[7m4\033[m - \033[32mEfetuar Transferencia\033[m')
    print('\033[7m5\033[m - \033[32mListar Contas\033[m')
    print('\033[7m6\033[m - \033[32mSair do sistema\033[m')

    opcao: int = int(input('\033[32mOpção:\033[m '))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('\033[36mVolte sempre!\033[m')
        sleep(2)
        exit(0)
    else:
        print('\033[31mOpção invalida!\033[m')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('\033[36mCriar Conta\033[m')

    nome: str = input('\033[7mNome do Cliente:\033[m ')
    email: str = input('\033[7mEmail:\033[m ')
    cpf: str = input('\033[7mCPF:\033[m ')
    data_nascimento: str = input('\033[7mData de nascimento:\033[m ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('\033[36mConta criada com sucesso!\033[m')
    print('\033[36mDados da conta:\033[m')
    print('\033[36m--------------------------\033[m')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('\033[32mNumero da conta:\033[m '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('\033[32mInforme o valor do saque:\033[m '))
            conta.sacar(valor)
        else:
            print(f'\033[31mNão foi encontrado a conta de numero {numero}\033[m')

    else:
        print('\033[31mAinda não há contas cadastradas!\033[m')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('\033[32mInforme o numero da conta:\033[m '))

        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('\033[32mInforme o valor:\033[m '))

            conta.depositar(valor)
    else:
        print(f'\033[31mAinda não há contas cadastradas\033[m')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('\033[32mInforme o numero da conta:\033[m '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('\033[32mInforme o numero da conta destino:\033[m '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('\033[32mInforme o valor:\033[m '))

                conta_o.tranferir(conta_d, valor)
            else:
                print(f'\033[32mA conta de numero {numero_d} não foi encontrada\033[m')
        else:
            print(f'\033[32mSua conta com numero {numero_o} não foi encontrado\033[m')
    else:
        print('\033[31mAinda não há conta cadastrada\033[m')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('\033[36mLista de contas\033[m')
        print('\033[36m---------------\033[m')

        for conta in contas:
            print(conta)
            print('\033[36m---------------\033[m')
            sleep(1)
    else:
        print('\033[32mAinda não existe conta cadastrada\033[m')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
