n = []
for i in range(20):
  y = int(input())
  n.append(y)
r = list(reversed(n))
for x in range(20):
  print(f'N[{x}] = {r[x]}')