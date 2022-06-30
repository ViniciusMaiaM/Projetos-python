# A(n+1) - An = 2n + 3 | n >= 0 e A0 = 1
# A(n+1) = 2n + 3 + An
# A = 2(n-1) + 3 + A(n-1)

print('Soluções da questão 1')
print('')
print('a: ')

an = 1

v = int(input('Insira um valor para a expressão: '))
print('')
for i in range(1, v+1):
    an = 2*(i-1) + 3 + an

print('Por looping: ', an)


def funca(n):
    if n == 0:
        return 1
    else:
        return 2*(n-1) + 3 + funca(n-1)


print('Por recursão: ', funca(v))
