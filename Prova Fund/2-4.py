#An+1 = 200+An*(1,06)
#An = 200+(A(n-1))*(1,06)
#A0 = 1000
import os
os.system('cls')
print ('Solução da pagina 2')
print ('Questão 4:')

mes = 47
ano = 1000

for i in range (1,mes+1):
  ano = 200+ano*1.06

print ("Por looping: ",ano)

def func4 (n):
  if n == 0:
    return 1000
  else:
    return 200+func4(n-1)*1.06

print ('Por função: ',  func4(mes))