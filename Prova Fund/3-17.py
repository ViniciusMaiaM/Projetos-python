import os
os.system('cls')
# An = 7An-1 - 10An-2 | a0 = 5 e a1 = 16


print ('Soluções da pagina 3')
print ('')
print ('Questão 17:')

an0 = 5
an1 = 16
r = 5

v = int(input('Insira um valor para a expressão: '))

if v == 1:
  r = 16
else:
  for i in range (2,v+1):
    r = 7*an1 - 10*an0 
    an0 = an1
    an1 = r

print ("Por looping: ",r)

def func3 (n):
  if n == 0:
    return 5
  elif n == 1:
    return 16  
  else:
    return 7*func3(n-1) - 10*func3(n-2)

print ('Por função: ',func3(v)) 