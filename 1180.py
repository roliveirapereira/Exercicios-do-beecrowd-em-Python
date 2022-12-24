n = int(input())
y = list(map(int, input().split()))

mn, pos = 10000000, 0

for x in range(n):
 if y[x] < mn:
   mn = y[x]
   pos = x
print(f'Menor valor: {mn}')
print(f'Posicao: {pos}')