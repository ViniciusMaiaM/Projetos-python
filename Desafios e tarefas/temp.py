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

for i in range (7): 
  if temps[i] > md:
    print ('A temperatura',temps[i],'foi maior do que a média no horário', hr[i] )
    contma += 1
  else:
    print ('A temperatura',temps[i], 'foi menor do que a média no horário', hr[i] )
    contme -= 1

print ('A temperatura foi maior do que média %d vezes' %(contma))
print ('A temperatura foi menor do que média %d vezes' %(contme))