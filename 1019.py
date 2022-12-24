segundos = int(input())

horas = int(segundos // 3600)
minutos = (segundos % 3600) //60
segundo_restantes =  segundos % 3600 % 60
print(f'{horas}:{minutos}:{segundo_restantes}')


