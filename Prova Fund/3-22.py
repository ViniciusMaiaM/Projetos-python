import os
os.system('cls')
# An = Ln-1 + Ln-2 | n>=3 e  L1 = 1 e L2 = 3


print ('Soluções da pagina 3')
print ('')
print ('Questão 22:')

l1 = 1
l2 = 3
r = 1

v = int(input('Insira um valor para a expressão: '))

if v == 2:
  r = 3
else:
  for i in range (3,v+1):
    r = l2+l1 
    l1 = l2
    l2 = r

print ("Por looping: ",r)

def func3 (n):
  if n == 1:
    return 1
  elif n == 2:
    return 3  
  else:
    return func3(n-1) + func3(n-2)

print ('Por função: ',func3(v)) 