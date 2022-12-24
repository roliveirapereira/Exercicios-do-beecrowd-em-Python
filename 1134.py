combustivel = int(input())
gasolina = 0
alcool = 0
diesel = 0
while combustivel != 4:
  if combustivel == 1:
    alcool += 1
  elif combustivel == 2:
    gasolina += 1
  elif combustivel == 3:
    diesel += 1
  combustivel = int(input())
print(f'MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')