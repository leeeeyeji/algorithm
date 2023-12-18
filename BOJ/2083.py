#럭비 클럽
while True:
  name,b,c=input().split()
  age=int(b)
  weg=int(c)
  if name=='#' and b=='0' and c=='0':
    break
  if(age>17 or weg>=80):
    print(name+' Senior')
  else:
    print(name+' Junior')