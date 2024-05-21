import os


def limparTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')