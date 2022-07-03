import os
os.system('cls')
# An+1 - 2An = 5 | n>=0 e A0 = 1
# An+1 = 5 + 2An
# An = 5 + 2A(n-1)

print('Soluções da questão 1')
print('Letra C:')

an = 1

v = int(input('Insira um valor para a expressão: '))

for i in range(1, v+1):
    an = 5 + 2*an
print('Por looping: ', an)


def funcc(n):
    if n == 0:
        return 1
    else:
        return 5 + 2*funcc(n-1)


print('Por função: ', funcc(v))
