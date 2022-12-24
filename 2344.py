nota = int(input())

if nota == 0:
 print(f'E')
elif nota == 1 or nota == 35 or nota < 35:
  print(f'D')
elif nota == 36 or nota ==60 or nota <60:
  print(f'C')
elif nota ==61 or nota ==85 or nota <85:
  print(f'B')
elif nota ==86 or nota ==100 or nota < 100:
  print(f'A')