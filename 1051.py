salary = float(input())

if salary <= 2000:
  print('Isento')
else:
 if salary <= 3000:
  imposto = (salary - 2000) * 8 / 100
  
 elif salary <= 4000:
  imposto = (salary - 3000 )* 18/100 + 80
  
 else:
  imposto = (salary - 4500 )* 28 / 100 + 80 + 270

 print(f'R$ {imposto:.2f}')
