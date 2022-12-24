p = input().split()
p1 = int(p[0])
c1 = int(p[1])
p2 = int(p[2])
c2 = int(p[3])

if p1 * c1 == p2 * c2:
  print(0)

elif p1 * c1 > p2 * c2:
  print(-1)

else:
  print(1)
  