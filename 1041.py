#ola galerinha do meu replit
#iae negao
# bora negão salvando geral
# negão me explia esse split pfvr 
#pq (v[0])
#posicao 0, vai pegar o primeiro valor 
#o v vai guardar 2 valores
#ai ele pega o primeiro valor de v(v[0])
#e dps pegaa o segundo(v[1])
#mas da pra fzr do outro jeito dboa
# x, y = input().split()
# x , y = float(x), float(y)
v = input().split()
x = float(v[0])
y = float(v[1])

if x == 0 and y == 0:
  print('Origem')
elif x == 0 and y != 0:
  print('Eixo Y')

elif x != 0 and y == 0:
  print('Eixo X')
  
elif x > 0 and y > 0:
  print('Q1')
  
elif x < 0 and y > 0:
  print('Q2')

elif x < 0 and y < 0:
  print('Q3')

elif x > 0 and y < 0:
  print('Q4')