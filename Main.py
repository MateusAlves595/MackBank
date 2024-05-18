#Imports das funções
from Funções.Cadastrar import cadastrar
from Funções.Depositar import depositar
from Funções.Sacar import sacar
from Funções.CosultarSaldo import consultarSaldo
from Funções.ConsultarExtrato import consultarExtrato
from Funções.AtualizarDados import atualizarDados

def menu():
    print("MACK BANK - ESCOLHA UMA OPÇÃO:\n (1) CADASTRAR CONTA CORRENTE\n (2) DEPOSITAR")
    print(" (3) SACAR\n (4) CONSULTAR SALDO\n (5) CONSULTAR EXTRATO\n (6) ATUALIZAR INFORMAÇÕES\n (7) FINALIZAR")
    escolha = int(input())
    
    if escolha < 1 or escolha > 7:
        print("ESCOLHA UMA OPÇÃO VÁLIDA")
        menu()
    elif escolha == 1:
        cadastrar()
    elif escolha == 2:
        depositar()
    elif escolha == 3:
        sacar()
    elif escolha == 4:
        consultarSaldo()
    elif escolha == 5:
        consultarExtrato()
    elif escolha == 6:
        atualizarDados()
    elif escolha == 7:
        print("MACK BANK - SOBRE\nEste programa foi desenvolvido por\nMateus Alves da Silva")
menu()