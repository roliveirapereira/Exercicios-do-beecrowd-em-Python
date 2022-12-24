numeros = input() .split()
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])

delta = b*b - 4 * a * c 


if  delta < 0 or a == 0:
 print('Impossivel calcular')
else:
 rdelta = delta**(1/2)
 x1 = ((-b + rdelta) / (a * 2))
 x2 = ((-b - rdelta) / (a * 2))
 print(f'R1 = {x1:.5f}')
 print(f'R2 = {x2:.5f}')