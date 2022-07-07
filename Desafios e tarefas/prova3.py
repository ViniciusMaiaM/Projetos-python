from math import log
ano = int(input('Insira a idade do cachorro em anos:\n'))
mes = int(input('Insira a idade do cachorro em meses:\n'))
idade = ano + (mes/12)
hm = (16*(log(idade))) + 31
idadef = round(hm)
print ('A idade do seu animal é %.1f'%(idadef))