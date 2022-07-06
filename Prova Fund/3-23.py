import os
os.system('cls')
# 9An = 6An-1 - An-2 | a0 = 6 e a1 = 5
# An = (6An-1 - An-2)/9

print ('Soluções da pagina 3')
print ('')
print ('Questão 23:')

an0 = 6 
an1 = 5
r = 6

v = int(input('Insira um valor para a expressão: '))

if v == 1:
  r = 5
else:
  for i in range (2,v+1):
    r = (6*an1 - an0 )/9
    an0 = an1
    an1 = r

print ("Por looping: ",r)

def func3 (n):
  if n == 0:
    return 6
  elif n == 1:
    return 5  
  else:
    return (6*func3(n-1) - func3(n-2))/9

print ('Por função: ',func3(v)) 