print('Insira 6 temperaturas\n')
lista = []
a = 0
for i in range(6):
    a += 1
    temp = float(input('Insira a %dº temperatura: ' % (a)))
    lista.append(temp)

print()
print('Lista Na ordem em que foi inserida:')
for i in range(6):
    print('Valor %d: %.1f' % (i+1, lista[i]))

print()
print('Lista invertida:')
for i in range(5, -1, -1):
    print('Valor %d: %.1f' % (i+1, lista[i]))

print()
for i in range(5):
    for j in range(i+1, 6):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print('Lista ordenada:')
print(lista)
# tem a função sort, mas o professor introduziu está maneira de se resover. pega o valor de i e depois o de j (i+1) e ai compara se é maior ou não. se maior, troca os valores para ordernar na ordem crescente, repetindo o processo até que se encerrem os números
print()
for i in range(5):
    for j in range(i+1, 6):
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print('Lista do menor pro maior:')
print(lista)
