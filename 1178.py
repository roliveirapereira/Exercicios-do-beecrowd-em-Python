n = []
x = float(input())
for i in range(100):
    n.append(x)
    x = x / 2
    print(f'N[{i}] = {n[i]:.4f}')
