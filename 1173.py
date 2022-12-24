n = []
i = 0
a = int(input())
n.append(a)
print(f'N[{i}] = {a}')
for i in range(1,10):
  a = a * 2
  n.append(a)
  print(f'N[{i}] = {n[i]}')