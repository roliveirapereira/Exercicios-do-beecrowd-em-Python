n = int(input())
leds = 0
for x in range(n):
  leds = 0
  n2 = input()
  for x in n2:
    if x == '1':
      leds += 2
    elif x == '2':
      leds += 5
    elif x == '3':
      leds += 5
    elif x == '4':
      leds += 4
    elif x == '5':
      leds += 5
    elif x == '6':
      leds += 6
    elif x == '7':
      leds += 3
    elif x == '8':
      leds += 7
    elif x == '9':
      leds += 6
    elif x == '0':
      leds += 6
    
  print(f'{leds} leds')

  