n = []
y = int(input())
while len(n) <= 999:
  for x in range(y):
    if len(n) <= 999:
      n.append(x)
for i in range(1000):
  print(f'N[{i}] = {n[i]}')
