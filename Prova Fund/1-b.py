import os
os.system('cls')
# An+1 - An = 3n² - n | n >= 0 e A0 = 3
# An+1 = 3n² - n + An
# A = 3((n-1)²) - n-1 + A (n-1)


print ('Soluções da questão 1')
print ('Letra B:')

an = 3

v = int(input('Insira um valor para a expressão: '))

for i in range (1,v+1):
  an = 3*((i-1)**2) - (i-1) + an
print ("Por looping: ",an)

def funcb (n):
  if n == 0:
    return 3
  else:
    return 3*((n-1)**2) - (n-1) + funcb(n-1)

print ('Por função: ',funcb(v))