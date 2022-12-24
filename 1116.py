vezes = int(input())

for x in range (vezes):
  nums = input().split()
  x = float(nums[0])
  y = float(nums[1])

  if y == 0:
    print('divisao impossivel')
  else:
    r = x/y
    print(r)