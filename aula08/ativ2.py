import os

def limpa_tela():
    os.system('cls')

def decoracao():
    print(30 * '=')


def calcula_peso(peso):
    return  float(peso - 100) * 4


limpa_tela()

decoracao()

print('INICIANDO O PROGRAMA')

decoracao()


peso = float(input('Digite o peso do pescado: '))
FIXO = 100
MULTA = 4   

if peso > 100:
    multa = calcula_peso(peso)
    print(f'O peso do peixe é maior que o permitido e você pagará {multa}$')
else:
    print('Você não pagará multa.')
