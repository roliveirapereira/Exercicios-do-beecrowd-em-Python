n = int(input())

for x in range(n):
  a = int(input())

  if a % 2== 0:
    if a > 0:
      print('EVEN POSITIVE')
    elif a < 0:
      print('EVEN NEGATIVE')
    else:
      print('NULL')

  else:
    if a < 0:
      print('ODD NEGATIVE')
    elif a > 0:
      print('ODD POSITIVE')
    else:
      print('NULL')