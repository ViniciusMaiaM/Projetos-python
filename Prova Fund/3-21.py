import os
os.system('cls')
# An = -8An-1 - 16An-2 | a0 = 2 e a1 = -20


print ('Soluções da pagina 3')
print ('')
print ('Questão 21:')

an0 = 2
an1 = -20
r = 2

v = int(input('Insira um valor para a expressão: '))

if v == 1:
  r = -20
else:
  for i in range (2,v+1):
    r = -8*an1 - 16*an0 
    an0 = an1
    an1 = r

print ("Por looping: ",r)

def func3 (n):
  if n == 0:
    return 2
  elif n == 1:
    return -20  
  else:
    return -8*func3(n-1) - 16*func3(n-2)

print ('Por função: ',func3(v)) 