import os
os.system('cls')
print ('Questão 2\n')
n = int (input('Insira um número para calcular seu quadrado:\n'))
sum = 0

for i in range (1,n+1):
  sum = sum + ((2*i)-1)

print ('O quadrado do número %d é %d' % (n,sum))