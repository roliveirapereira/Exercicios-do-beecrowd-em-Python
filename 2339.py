inf = input() .split()
competidores = int(inf[0])
folhas = int(inf[1])
folhas_competidores = int(inf[2])

if folhas / competidores == folhas_competidores or folhas / competidores > folhas_competidores:
  print(f'S')
else: print(f'N')