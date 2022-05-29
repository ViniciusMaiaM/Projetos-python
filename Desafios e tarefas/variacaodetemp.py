from cProfile import label
import matplotlib.pyplot  # importar biblioteca do grafico
import random
print('Madrugada')
for a in range(1):  # Horários da madrugada
    h0 = random.uniform(22, 22)
    print('%.2f' % h0)
for b in range(1):
    h1 = random.uniform(22, 23)
    print('%.2f' % h1)
for c in range(1):
    h2 = random.uniform(23, 23)
    print('%.2f' % h2)
for d in range(1):
    h3 = random.uniform(23, 24)
    print('%.2f' % h3)
for e in range(1):
    h4 = random.uniform(24, 24)
    print('%.2f' % h4)
print('Manhã')
for f in range(1):  # Horários da Manhã
    h5 = random.uniform(24, 25)
    print('%.2f' % h5)
for g in range(1):
    h6 = random.uniform(25, 26)
    print('%.2f' % h6)
for h in range(1):
    h7 = random.uniform(26, 27)
    print('%.2f' % h7)
for i in range(1):
    h8 = random.uniform(27, 28)
    print('%.2f' % h8)
for j in range(1):
    h9 = random.uniform(28, 29)
    print('%.2f' % h9)
for k in range(1):
    h10 = random.uniform(29, 30)
    print('%.2f' % h10)
print('Tarde')
for l in range(1):  # Horários da Tarde
    h11 = random.uniform(30, 30)
    print('%.2f' % h11)
for m in range(1):
    h12 = random.uniform(30, 30)
    print('%.2f' % h12)
for n in range(1):
    h13 = random.uniform(30, 29)
    print('%.2f' % h13)
for o in range(1):
    h14 = random.uniform(29, 28)
    print('%.2f' % h14)
for p in range(1):
    h15 = random.uniform(28, 27)
    print('%.2f' % h15)
for q in range(1):
    h16 = random.uniform(27, 26)
    print('%.2f' % h16)
print('Noite')

for r in range(1):  # Horários da noite
    h17 = random.uniform(27, 26)
    print('%.2f' % h17)
for s in range(1):
    h18 = random.uniform(26, 26)
    print('%.2f' % h18)
for t in range(1):
    h19 = random.uniform(26, 25)
    print('%.2f' % h19)
for u in range(1):
    h20 = random.uniform(25, 24)
    print('%.2f' % h20)
for v in range(1):
    h21 = random.uniform(24, 23)
    print('%.2f' % h21)
for w in range(1):
    h22 = random.uniform(23, 22)
    print('%.2f' % h22)
for x in range(1):
    h23 = random.uniform(22, 22)
    print('%.2f' % h23)


horas = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']  # lista das horas
horas2 = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
          '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
temp = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11,
        h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23]
media = (h0+h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12 +
         h13+h14+h15+h16+h17+h18+h19+h20+h21+h22+h23)/24
media24 = []
print(media)

for z in range(24):
    media24.append(media)  # passando o valor de média para média 24

# definindo x e y I label dá o nome na legenda
matplotlib.pyplot.plot(horas, temp, label='Variação de temperatura')
# definindo a media no meio do gráfico
matplotlib.pyplot.plot(horas2, media24, 'red', label='Média')
matplotlib.pyplot.title('Variação de calor em Caicó')  # título
matplotlib.pyplot.xlabel('Horas')  # nome da linha x
matplotlib.pyplot.ylabel('Temperatura em Cº')  # nome da linha y
matplotlib.pyplot.legend()  # legenda
matplotlib.pyplot.show()

# madruga 22, 24
# manha 24,30 crescendo
# tarde 30,26 descendo
# noite 26,22 descendo