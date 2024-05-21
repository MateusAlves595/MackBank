#Imports das funções
import Funcoes.Cadastrar as Cadastrar
import Funcoes.Depositar as Depositar 
import Funcoes.Sacar as Sacar 
import Funcoes.ConsultarSaldo as ConsultarSaldo
import Funcoes.ConsultarExtrato as ConsultarExtrato
import Funcoes.AtualizarDados as AtualizarDados

from Funcoes.Cadastrar import contaCadastrada

def menu():
    print("MACK BANK - ESCOLHA UMA OPÇÃO:\n (1) CADASTRAR CONTA CORRENTE\n (2) DEPOSITAR")
    print(" (3) SACAR\n (4) CONSULTAR SALDO\n (5) CONSULTAR EXTRATO\n (6) ATUALIZAR INFORMAÇÕES\n (7) FINALIZAR")
    escolha = input("Sua opção: ")
    
    if escolha == '' or not escolha.isdigit():
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
        menu()
    else:
        opcao = int(escolha)
    
    if opcao < 1 or opcao > 7:
        print("OPCAO INVALIDA")   
    elif opcao == 1 and contaCadastrada == 1:
        print()
        print("CONTA JÁ CADASTRADA")
        print() 
    elif opcao == 1:
        Cadastrar.cadastrar()
    elif escolha == 2:
        Depositar.depositar()
    elif escolha == 3:
        Sacar.sacar()
    elif escolha == 4:
        ConsultarSaldo.consultarSaldo()
    elif escolha == 5:
        ConsultarExtrato.consultarExtrato()
    elif escolha == 6:
        AtualizarDados.atualizarDados()
    elif escolha == 7:
        print("MACK BANK - SOBRE\nEste programa foi desenvolvido por\nMateus Alves da Silva")
menu()