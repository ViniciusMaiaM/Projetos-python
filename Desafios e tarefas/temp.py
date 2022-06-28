# Escreva um programa em Python que leia um conjunto de medidas de temperatura de um paciente internado ao longo de um determinado dia. As medições devem ser feitas a cada três horas.
# A seguir, calcule a temperatura média do dia e exiba esse valor na tela.
# Por fim, verifique e indique quantas vezes e em quais horários a temperatura ficou acima da temperatura média do dia.


soma = 0
temps = []
ax = []
hr = []
soma = 0

for b in range(8):
    temp = float(input('Insira o valor da temperatura %d: ' % (b+1)))
    soma += temp
    time = float(input('Insira a hora em que essa temperatura foi medida %d: ' % (b+1)))
    temps.append (temp)
    hr.append (time)

md = soma/8

print (md)
contma = 0
contme = len(temps)

for temperatura in temps: 
  if temperatura > md:
    print ('A temperatura %.2f foi maior do que a média no horário %f' %(temperatura, hr))
    contma += 1
  else:
    print ('A temperatura %.2f foi menor do que a média no horário %f' %(temperatura,temperatura+1))
    contme -= 1

print ('A temperatura foi maior do que média %d' %(contma))
print ('A temperatura foi menor do que média %d' %(contme))