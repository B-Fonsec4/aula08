def calcula(num):
    dobro = num * 2
    # print(dobro)
    triplo = num * 3
    # print(triplo)
    return dobro, triplo
    # dobro = num * 2
    # return dobro
#parte principal
num = float(input('Digite o número: '))


x2, x3 = calcula(num)
print(f'O dobro é {x2} e o triplo é{x3}')
