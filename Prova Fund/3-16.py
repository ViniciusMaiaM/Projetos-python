import os
os.system('cls')
# An = 2An-1 + 8An-2 | a0 = 4 e a1 = 10


print ('Soluções da pagina 3')
print ('')
print ('Questão 16:')

an0 = 4
an1 = 10
r = 4

v = int(input('Insira um valor para a expressão: '))

if v == 1:
  r = 10
else:
  for i in range (2,v+1):
    r = 2*an1 + 8*an0 
    an0 = an1
    an1 = r

print ("Por looping: ",r)

def func3 (n):
  if n == 0:
    return 4
  elif n == 1:
    return 10  
  else:
    return 2*func3(n-1) + 8*func3(n-2)

print ('Por função: ',func3(v)) 