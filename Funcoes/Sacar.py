import Main
from Funcoes.LimparTerminal import limparTerminal
from Funcoes.Cadastrar import contaCliente
from Funcoes.Cadastrar import nomeCliente
from Funcoes.Cadastrar import historicoCliente
from Funcoes.Cadastrar import senhaCliente
from Funcoes.Cadastrar import limiteCliente
from Funcoes.Cadastrar import saldoCliente

erros = 0

#validações
def validarEntrada(entrada):
    global erros
    if entrada == '' or not entrada.isdigit():
        return False
    else:
        return True

def sacar():
    limparTerminal()
    print("MACK BANK - SAQUE EM CONTA")
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
    
    
    senha = input("INFORME A SENHA: ")
    if senha != senhaCliente[cliente]:
        print("SENHA INCORRETA")
        erros += 1
        Main.menu()
        
    valorSaque = input("VALOR DO SAQUE: R$ ")
    if valorSaque == '':
        print("VALOR INVALIDO")
        Main.menu()
    valorSaque = float(valorSaque)
    if valorSaque <= 0:
        print("VALOR DEVE SER MAIOR DO QUE R$ 0")
        Main.menu()
        
    if valorSaque > saldoCliente[cliente]:
        if valorSaque > limiteCliente[cliente] + saldoCliente[cliente]:
            print("SALDO INSUFICIENTE")
            Main.menu()
        print("VOCÊ ESTÁ UTILIZANDO SEU LIMITE DE CRÉDITO")
        input("SAQUE REALIZADO COM SUCESSO")
        limite = valorSaque - saldoCliente[cliente]
        saldoCliente[cliente] = 0
        limiteCliente[cliente] -= limite
        historicoCliente.append(-valorSaque)
        Main.menu()
    saldoCliente[cliente] -= valorSaque
    historicoCliente.append(-valorSaque)
    input("SAQUE REALIZADO COM SUCESSO")
    Main.menu()
    
        
    