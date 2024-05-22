from cmath import isnan
import random
import re
from pycpfcnpj import cpfcnpj
import Funcoes.LimparTerminal as LimparTerminal

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

def cadastrar():
    global contaCliente, historicoCliente, nomeCliente, telefoneCliente, contaCadastrada, emailCliente, saldoCliente, limiteCliente, senhaCliente, cpfCliente
    numeroAleatorio = random.randint(1000, 9999)
    LimparTerminal.limparTerminal()
    print("MACK BANK - CADASTRO DE CONTA")
    print()
    print("NÚMERO DA CONTA: ", end="")
    print(numeroAleatorio)
    print()
    contaCliente.append(numeroAleatorio)
    nome = input("NOME DO CLIENTE: ")
    print()
    if validarNome(nome) == False:
        print("NOME INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        return
    nomeCliente.append(nome)
    
    telefone = input("TELEFONE.......: ")
    print()
    if validarTelefone(telefone) == False:
        print("NUMERO INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        return
    telefoneCliente.append(telefone)
    
    email = input("EMAIL: ")
    print()
    if validarEmail(email) == False:
        print('EMAIL INVÁLIDO')
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        return
    emailCliente.append(email)
    
    cpf = input('CPF: ')
    print()
    if not cpfcnpj.validate(cpf):
        print("CPF INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        return
    cpfCliente.append(cpf)
    
    saldo = int(input("SALDO INICIAL: R$ "))
    print()
    if validarSaldoInicial(saldo) == False:
        print('SALDO INICIAL INVÁLIDO, DEVE SER UM NÚMERO MAIOR OU IGUAL A 1000')
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        saldoCliente = []
        return
    novoSaldo = float(saldo)
    saldoCliente.append(novoSaldo)
    
    limite = int(input("LIMITE DE CRÉDITO: R$ "))
    print()
    if validarLimite(limite) == False:
        print('LIMITE INVÁLIDO, DEVE SER MAIOR OU IGUA A 0')
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        saldoCliente = []
        limiteCliente = []
        return
    novoLimite = float(limite)
    limiteCliente.append(novoLimite)
    
    senha = input('SENHA...: ')
    if validarSenha(senha) == False:
        print("SENHA INVÁLIDA, DEVE CONTER 6 CARACTERES")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        saldoCliente = []
        limiteCliente = []
        senhaCliente = []
        return
    else:
        senhaDupla = input('REPITA A SENHA...: ')
        if senhaDupla != senha:
            print('DÍGITE A SENHA CORRETAMENTE')
            contaCliente = []
            nomeCliente = []
            telefoneCliente = []
            emailCliente = []
            cpfCliente = []
            saldoCliente = []
            limiteCliente = []
            return
        else:
            senhaCliente.append(senha)
    print()
    input("CADASTRO REALIZADO! PRESSIONE UME TECLA PARA VOLTAR AO MENU...")
    contaCadastrada = 1
    