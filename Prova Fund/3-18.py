import os
os.system('cls')
# An*2 = 7An-1 - 3An-2 | a0 = a1 = 1
# An = (7A(n-1) - 3A(n-2))/2

print ('Soluções da pagina 3')
print ('')
print ('Questão 18:')

an0 = 1
an1 = 1
r = 1

v = int(input('Insira um valor para a expressão: '))

for i in range (2,v+1):
  r = (7*an1 - 3*an0)/2
  an0 = an1
  an1 = r

print ("Por looping: ",r)

def func3 (n):
  if n == 0 or n == 1:
    return 1
  else:
    return (7*func3(n-1) - 3*func3(n-2))/2

print ('Por função: ',func3(v)) 