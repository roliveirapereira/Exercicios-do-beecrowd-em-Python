nums = input().split()
x = int(nums[0])
y = int(nums[1])

while x != 0 and y != 0:
  if x > 0 and y > 0:
      print('primeiro')
    
  elif x < 0 and y < 0:
      print('terceiro')
    
  elif x < 0 and y > 0:
      print('segundo')
    
  else: 
      print('quarto')

  nums = input().split()
  x = int(nums[0])
  y = int(nums[1])