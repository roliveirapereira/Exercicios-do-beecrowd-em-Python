a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
v = 0

quantidade = 0
# a quantidade e uma variavel de contagem
if a > 0:
  quantidade = quantidade + 1
  v = v + a
  
if b > 0:
  quantidade = quantidade + 1
  v = v + b
  
if c > 0:
  quantidade = quantidade + 1
  v = v + c
  
if d > 0:
  quantidade = quantidade + 1
  v = v + d
  
if e > 0:
  quantidade = quantidade + 1
  v = v + e
  
if f > 0:
  quantidade = quantidade + 1
  v = v + f
  
media = v / quantidade

print(quantidade, 'valores positivos')
print(f'{media:.1f}')