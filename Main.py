from cmath import isnan
import random
import re
from pycpfcnpj import cpfcnpj
import os

#funções de validação
def validarNome(nome):
    if nome == '':
        return False
    else:
        return True

def validarTelefone(numero):
    padrão = r"\d{5}-\d{4}"
    result = re.search(padrão, numero)
    
    if result:
        return True
    else:
        return False

def validarEmail(email):
    if '@' and '.com' in email:
        return True
    else:
        return False

def validarSaldoInicial(saldo):
    if saldo < 1000 or isnan(saldo):
        return False
    else:
        return True
        
def validarLimite(limite):
    if limite < 0 or isnan(limite):
        return False
    else:
        return True

def validarSenha(senha):
    if len(senha) < 6 or len(senha) > 6:
        return False
    else:
        return True

def validarEntrada(entrada):
    if not entrada.isdigit():
        return False
    else:
        return True
    
def validarValor(valor):
    if valor <= 0 :
        return False
    else:
        return True

def limparTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')
    
#Variáveis
contaCliente = []
nomeCliente = []
telefoneCliente = []
emailCliente = []
saldoCliente = []
limiteCliente = []
senhaCliente = []
cpfCliente = []
contaCadastrada = 0
historicoCliente = []
erros = 0

def cadastrar():
    global contaCliente, historicoCliente, nomeCliente, telefoneCliente, contaCadastrada, emailCliente, saldoCliente, limiteCliente, senhaCliente, cpfCliente
    numeroAleatorio = random.randint(1000, 9999)
    limparTerminal()
    print("MACK BANK - CADASTRO DE CONTA")
    print()
    print("NÚMERO DA CONTA: ", end="")
    print(numeroAleatorio)
    print()
    contaCliente.append(numeroAleatorio)
    nome = input("NOME DO CLIENTE: ")
    print()
    if validarNome(nome) == False:
        input("NOME INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        menu()
    nomeCliente.append(nome)
    
    telefone = input("TELEFONE.......: ")
    print()
    if validarTelefone(telefone) == False:
        input("NUMERO INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        menu()
    telefoneCliente.append(telefone)
    
    email = input("EMAIL: ")
    print()
    if validarEmail(email) == False:
        input('EMAIL INVÁLIDO')
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        menu()
    emailCliente.append(email)
    
    cpf = input('CPF: ')
    print()
    if not cpfcnpj.validate(cpf):
        input("CPF INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        menu()
    cpfCliente.append(cpf)
    
    saldo = int(input("SALDO INICIAL: R$ "))
    print()
    if validarSaldoInicial(saldo) == False:
        input('SALDO INICIAL INVÁLIDO, DEVE SER UM NÚMERO MAIOR OU IGUAL A 1000')
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        saldoCliente = []
        menu()
    novoSaldo = float(saldo)
    saldoCliente.append(novoSaldo)
    
    limite = int(input("LIMITE DE CRÉDITO: R$ "))
    print()
    if validarLimite(limite) == False:
        input('LIMITE INVÁLIDO, DEVE SER MAIOR OU IGUA A 0')
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        saldoCliente = []
        limiteCliente = []
        menu()
    novoLimite = float(limite)
    limiteCliente.append(novoLimite)
    
    senha = input('SENHA...: ')
    if validarSenha(senha) == False:
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        saldoCliente = []
        limiteCliente = []
        senhaCliente = []
        input("SENHA INVÁLIDA, DEVE CONTER 6 CARACTERES")
        menu()
    else:
        senhaDupla = input('REPITA A SENHA...: ')
        if senhaDupla != senha:
            contaCliente = []
            nomeCliente = []
            telefoneCliente = []
            emailCliente = []
            cpfCliente = []
            saldoCliente = []
            limiteCliente = []
            input('DÍGITE A SENHA CORRETAMENTE')
            menu()
        else:
            senhaCliente.append(senha)
    print()
    input("CADASTRO REALIZADO!")
    contaCadastrada = 1
    menu()

def depositar():
    limparTerminal()
    print("MACK BANK - DEPOSITO EM CONTA")
    print()
    
    codigo = input("INFORME O NÚMERO DA CONTA: ")
    if codigo == '':
        input("NUMERO DE CONTA INVÁLIDO")
        menu()
    if validarEntrada(codigo) == False:
        input("NÚMERO INVÁLIDO")
        menu()
    codigo = int(codigo)
    if codigo not in contaCliente:
        input("NÃO EXISTE UMA CONTA COM ESSE NÚMERO")
        menu()
    
    
    cliente = contaCliente.index(codigo)
    print("NOME DO CLIENTE: ", nomeCliente[cliente])
    print()
    
    valorDeposito = input("VALOR DO DEPÓSITO: R$ ")
    if valorDeposito == '':
        input("POR FAVOR DÍGITE UM VALOR")
        menu()
    if validarValor(int(valorDeposito)) == False:
        input("VALOR DEVE SER MAIOR DO QUE R$ 0")
        input()
        menu()
    saldoCliente[cliente] += int(valorDeposito)
    historicoCliente.append(int(valorDeposito))
    print()
    input("DEPÓSITO REALIZADO COM SUCESSO")
    menu()

def sacar():
    global erros
    limparTerminal()
    print("MACK BANK - SAQUE EM CONTA")
    print()
    
    codigo = input("INFORME O NÚMERO DA CONTA: ")
    if codigo == '':
        input("NUMERO DE CONTA INVÁLIDO")
        menu()
    if validarEntrada(codigo) == False:
        input("NÚMERO INVÁLIDO")
        menu()
    codigo = int(codigo)
    if codigo not in contaCliente:
        input("NÃO EXISTE UMA CONTA COM ESSE NÚMERO")
        menu()
    
    
    cliente = contaCliente.index(codigo)
    print("NOME DO CLIENTE: ", nomeCliente[cliente])
    print()
    
    
    senha = input("INFORME A SENHA: ")
    if senha != senhaCliente[cliente]:
        input("SENHA INCORRETA")
        erros += 1
        menu()
        
    valorSaque = input("VALOR DO SAQUE: R$ ")
    if valorSaque == '':
        input("VALOR INVALIDO")
        menu()
    valorSaque = float(valorSaque)
    if valorSaque <= 0:
        input("VALOR DEVE SER MAIOR DO QUE R$ 0")
        menu()
        
    if valorSaque > saldoCliente[cliente]:
        if valorSaque > limiteCliente[cliente] + saldoCliente[cliente]:
            input("SALDO INSUFICIENTE")
            menu()
        print("VOCÊ ESTÁ UTILIZANDO SEU LIMITE DE CRÉDITO")
        input("SAQUE REALIZADO COM SUCESSO")
        limite = valorSaque - saldoCliente[cliente]
        saldoCliente[cliente] = 0
        limiteCliente[cliente] -= limite
        historicoCliente.append(-valorSaque)
        menu()
    saldoCliente[cliente] -= valorSaque
    historicoCliente.append(-valorSaque)
    input("SAQUE REALIZADO COM SUCESSO")
    menu()

def consultarSaldo():
    global erros
    limparTerminal()
    print("MACK BANK - CONSULTA DE SALDO")
    print()
    
    codigo = input("INFORME O NÚMERO DA CONTA: ")
    if codigo == '':
        input("NUMERO DE CONTA INVÁLIDO")
        menu()
    if validarEntrada(codigo) == False:
        input("NÚMERO INVÁLIDO")
        menu()
    codigo = int(codigo)
    if codigo not in contaCliente:
        input("NÃO EXISTE UMA CONTA COM ESSE NÚMERO")
        menu()
    
    cliente = contaCliente.index(codigo)
    print("NOME DO CLIENTE: ", nomeCliente[cliente])
    print()
    senha = input("INFORME A SENHA: ")
    if senha != senhaCliente[cliente]:
        print("SENHA INCORRETA")
        erros += 1
        menu()
    print(f"SALDO EM CONTA: R$ {saldoCliente[cliente]:.2f}")
    print(f"LIMITE DE CRÉDITO: R$ {limiteCliente[cliente]:.2f}")
    input("PRESSIONE UMA TECLA PARA RETORNAR AO MENU")
    menu()

def consultarExtrato():
    global erros
    limparTerminal()
    print("MACK BAK - EXTRATO DA CONTA")
    print()
    
    codigo = input("INFORME O NÚMERO DA CONTA: ")
    if codigo == '':
        input("NUMERO DE CONTA INVÁLIDO")
        menu()
    if validarEntrada(codigo) == False:
        input("NÚMERO INVÁLIDO")
        menu()
    codigo = int(codigo)
    if codigo not in contaCliente:
        input("NÃO EXISTE UMA CONTA COM ESSE NÚMERO")
        menu()
    
    cliente = contaCliente.index(codigo)
    print("NOME DO CLIENTE: ", nomeCliente[cliente])
    print()
    senha = input("INFORME A SENHA: ")
    if senha != senhaCliente[cliente]:
        print("SENHA INCORRETA")
        erros += 1
        menu()
    
    print(f"LIMITE DE CRÉDITO: R$ {limiteCliente[cliente]:.2f}")
    print()
    print("ULTIMAS OPERAÇÕES")
    for i in historicoCliente:
        if i < 0:
            print(f"\nSAQUE: R$ {i:.2f}")
        else:
            print(f"\nDEPÓSITO: R$ {i:.2f}")
    print(f"SALDO EM CONTA: R$ {saldoCliente[cliente]:.2f}")
    print()
    if saldoCliente[cliente] <= 0:
        print("ATENÇÃO: VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")
    input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU")
    menu()

def menu():
    limparTerminal()
    print("MACK BANK - ESCOLHA UMA OPÇÃO:\n (1) CADASTRAR CONTA CORRENTE\n (2) DEPOSITAR")
    print(" (3) SACAR\n (4) CONSULTAR SALDO\n (5) CONSULTAR EXTRATO\n (6) FINALIZAR")
    escolha = input("Sua opção: ")
    
    if escolha == '' or not escolha.isdigit():
        input("ESCOLHA UMA OPÇÃO VÁLIDA")
        menu()
    else:
        opcao = int(escolha)
    
    if opcao < 1 or opcao > 6:
        input("OPCAO INVALIDA")   
        menu()
    elif opcao == 1 and contaCadastrada == 1:
        print()
        input("CONTA JÁ CADASTRADA")
        menu() 
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        depositar()
    elif opcao == 3 and erros == 3:
        input("SUA CONTA ESTÁ BLOQUEADA")
    elif opcao == 3 and erros < 3:
        sacar()
    elif opcao == 4 and erros == 3:
        input("SUA CONTA ESTÁ BLOQUEADA")
    elif opcao == 4 and erros < 3:
        consultarSaldo()
    elif opcao == 5 and erros == 3:
        input("SUA CONTA ESTÁ BLOQUEADA")
    elif opcao == 5 and erros < 3:
        consultarExtrato()
    elif opcao == 6:
        limparTerminal()
        print("MACK BANK - SOBRE\nEste programa foi desenvolvido por Mateus Alves da Silva")
        os.kill
menu()