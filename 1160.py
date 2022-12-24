m = int(input())
for x in range(m):
 n = input().split()
 pa = int(n[0])
 pr = int(n[1])
 a = float(n[2])
 b = float(n[3])
 anos = 0
 while pa<=pr:
   pa = pa + (pa*a//100)
   pr = pr + (pr*b//100)
   anos += 1
   if pa > pr:
     if anos>100:
       print('Mais de 1 seculo.')
     else:
       print(anos,'anos.')
  