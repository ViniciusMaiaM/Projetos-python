import os
os.system('cls')
#An+1 - 2An = 2**n | n>=0, A0 = 1
#An+1 = 2**n + 2An
#An = 2**(n-1) + 2A(n-1)

print ('Soluções da questão 1')
print ('Letra D:')

an = 1

v = int(input('Insira um valor para a expressão: '))

for i in range (1,v+1):
  an = (2**(i-1)) + 2*an
print ('Por looping: ',an)

def funcd (n):
  if n == 0:
    return 1
  else:
    return (2**(n-1)) + 2*funcd(n-1) 

print ('Por função: ', funcd(v))