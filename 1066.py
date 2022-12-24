a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

pa = 0
po = 0
vn = 0
if a % 2 == 0:
 pa = pa + 1

if b % 2 == 0:
 pa = pa + 1

if c % 2 == 0:
 pa = pa + 1

if d % 2 == 0:
 pa = pa + 1

if e % 2 == 0:
 pa = pa + 1

if a == 0:
  po = po
elif a > 0:
  po = po + 1
  
if b == 0:
  po = po
elif b > 0:
  po = po + 1
  
if c == 0:
  po = po
elif c > 0:
  po = po + 1
  
if d == 0:
  po = po
elif d > 0:
  po = po + 1
  
if e == 0:
  po = po
elif e > 0:
  po = po + 1

if a < 0:
  vn = vn + 1

if b < 0:
  vn = vn + 1

if c < 0:
  vn = vn + 1

if d < 0:
  vn = vn + 1

if e < 0:
  vn = vn + 1

print(f'{pa} valor(es) par(es)')
print(f'{5 - pa} valor(es) impar(es)')
print(f'{po} valor(es) positivo(s)')
print(f'{vn} valor(es) negativo(s)')
      