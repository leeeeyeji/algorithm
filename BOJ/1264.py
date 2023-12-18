#모음의 개수
m = ['a', 'e', 'i', 'o', 'u']
n = ['A', 'E', 'I', 'O', 'U']

while True:
  count = 0
  s = input()
  if s == '#':
    break
  for c in s:
    if c in m or c in n:
      count += 1
  print(count)