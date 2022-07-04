import os
os.system('cls')
# An = 6An-1 - 8An-2 | a0 = 1 e a1 = 0


print ('Soluções da pagina 3')
print ('')
print ('Questão 15:')

an0 = 1
an1 = 0
r = 1

v = int(input('Insira um valor para a expressão: '))

if v == 1:
  r = 0
else:
  for i in range (2,v+1):
    r = 6*an1 - 8*an0 
    an0 = an1
    an1 = r

print ("Por looping: ",r)

def func3 (n):
  if n == 0:
    return 1
  elif n == 1:
    return 0  
  else:
    return 6*func3(n-1) - 8*func3(n-2)

print ('Por função: ',func3(v))