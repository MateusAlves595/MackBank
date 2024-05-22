import Main
from Funcoes.LimparTerminal import limparTerminal
from Funcoes.Cadastrar import contaCliente
from Funcoes.Cadastrar import nomeCliente
from Funcoes.Cadastrar import saldoCliente
from Funcoes.Cadastrar import historicoCliente

#validações
def validarEntrada(entrada):
    if entrada == '' or not entrada.isdigit():
        return False
    else:
        return True
    
def validarValor(valor):
    if valor <= 0 :
        return False
    else:
        return True


def depositar():
    limparTerminal()
    print("MACK BANK - DEPOSITO EM CONTA")
    print()
    
    codigo = input("INFORME O NÚMERO DA CONTA: ")
    if validarEntrada(codigo) == False:
        print("NUMERO DE CONTA INVÁLIDO")
        Main.menu()
    
    codigo = int(codigo)
    if codigo not in contaCliente:
        print("NÃO EXISTE UMA CONTA COM ESSE NÚMERO")
        Main.menu()
    
    
    cliente = contaCliente.index(codigo)
    print("NOME DO CLIENTE: ", nomeCliente[cliente])
    print()
    
    valorDeposito = input("VALOR DO DEPÓSITO: R$ ")
    if valorDeposito == '':
        print("POR FAVOR DÍGITE UM VALOR")
        Main.menu()
    if validarValor(int(valorDeposito)) == False:
        print("VALOR DEVE SER MAIOR DO QUE R$ 0")
        input()
        Main.menu()
    saldoCliente[cliente] += int(valorDeposito)
    historicoCliente.append(int(valorDeposito))
    print()
    input("DEPÓSITO REALIZADO COM SUCESSO")
    Main.menu()
    