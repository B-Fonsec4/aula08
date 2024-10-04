import os
import random


def limpa_tela():
    os.system('cls')


def decoracao():
    print(12*'=')

# def gera_numeros(a, b):
#     return

# gera_numeros()
    
# def gera_numeros( , , 2):
def gera_numeros():
    n1 = random.randint(1, 100)
    n2 = random.randint(2, 50)
    return n1, n2

def soma(n1, n2):
    adicao = n1 + n2
    return adicao


def sub(n1, n2):
    sub = n1 - n2
    return sub


def mult(n1, n2):
    mult = n1 * n2
    return mult


def div(n1, n2):
    div = n1 / n2
    return div
    




limpa_tela()
decoracao()
print( 'CALCULADORA')




n1, n2= gera_numeros()

mais = soma(n1, n2)


menos = sub(n1, n2)


vezes = mult(n1, n2)


divisao = div(n1, n2)

total = mais , menos , vezes , divisao
print(f' Os números são {n1} e {n2} a soma é {mais}, a subtração é {menos} a multiplicação e {vezes} e a divisão é {divisao}')

