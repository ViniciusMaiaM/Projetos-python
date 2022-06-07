listatemp = []

for i in range(8):
    l = float(input('Insira a %dº temperatura: ' % (i+1)))
    listatemp += [l]
print(listatemp)

soma = 0
tam = len(listatemp)  # len vê a quantidade de termos presentes na lista

for valor in (listatemp):  # o laço roda igual ao número de termos da lista e pega cada valor
    soma += valor

media = soma/tam
print(media)
