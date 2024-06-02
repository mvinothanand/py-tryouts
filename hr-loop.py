strings = []

for _ in range(0, int(input())):
  strings.append(input())

for string in strings:
  even = ''
  odd = ''
  
  for i in range(0, len(string)):
    if i + 1 == 1:
      odd += string[i]
    elif (i+1) % 2 == 0:
      even += string[i]
    else:
      odd += string[i]

  print(odd, even)
  