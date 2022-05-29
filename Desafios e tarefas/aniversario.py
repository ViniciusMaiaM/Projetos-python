import datetime
# importando a biblioteca

print('Olá, o programa a seguir ira calcular sua idade, informe os dados requisitados!\n')
dia_nasc = int(input('Informe o dia do seu nascimento:\n'))
mes_nasc = int(input('Informe o mês do seu nascimento:\n'))
ano_nasc = int(input('Informe o ano do seu nascimento:\n'))

dia = datetime.date.today().day
mes = datetime.date.today().month
ano = datetime.date.today().year
# utilizando a biblioteca importada

if mes == mes_nasc and dia > dia_nasc or mes > mes_nasc:
    idade1 = ano-ano_nasc
    print('Sua idade é', idade1)  # caso já tenha completado aniversário

elif mes == mes_nasc and dia == dia_nasc:
    idade2 = ano-ano_nasc
    # caso esteja fazendo aniversário no dia
    print('Feliz aniversário, sua idade é', idade2)

else:
    idade3 = (ano-ano_nasc)-1
    # caso ainda não tenha completado aniversário
    print('vSua idade é', idade3)
