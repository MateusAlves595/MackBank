#Imports das funções
from Funcoes.Cadastrar import cadastrar
from Funcoes.Depositar import depositar 
from Funcoes.Sacar import sacar 
from Funcoes.ConsultarSaldo import consultarSaldo
from Funcoes.ConsultarExtrato import consultarExtrato
from Funcoes.Sacar import erros

from Funcoes.Cadastrar import contaCadastrada

def menu():
    print("MACK BANK - ESCOLHA UMA OPÇÃO:\n (1) CADASTRAR CONTA CORRENTE\n (2) DEPOSITAR")
    print(" (3) SACAR\n (4) CONSULTAR SALDO\n (5) CONSULTAR EXTRATO\n (6) FINALIZAR")
    escolha = input("Sua opção: ")
    
    if escolha == '' or not escolha.isdigit():
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
        menu()
    else:
        opcao = int(escolha)
    
    if opcao < 1 or opcao > 6:
        print("OPCAO INVALIDA")   
    elif opcao == 1 and contaCadastrada == 1:
        print()
        print("CONTA JÁ CADASTRADA")
        print() 
    elif opcao == 1:
        cadastrar()
    elif opcao == 2:
        depositar()
    elif opcao == 3 and erros == 3:
        print("SUA CONTA ESTÁ BLOQUEADA")
    elif opcao == 3 and erros < 3:
        sacar()
    elif opcao == 4 and erros == 3:
        print("SUA CONTA ESTÁ BLOQUEADA")
    elif opcao == 4 and erros < 3:
        consultarSaldo()
    elif opcao == 5 and erros == 3:
        print("SUA CONTA ESTÁ BLOQUEADA")
    elif opcao == 5 and erros < 3:
        consultarExtrato()
    elif opcao == 6:
        print("MACK BANK - SOBRE\nEste programa foi desenvolvido por\nMateus Alves da Silva")
menu()