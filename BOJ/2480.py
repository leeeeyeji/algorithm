#주사위 새개

a,b,c=map(int,input().split())
prize=0
max=0

if(a==b==c):
  prize=10000+a*1000
elif(a==b):
  prize=1000+100*a
elif(a==c):
  prize=1000+100*c
elif(b==c):
  prize=1000+100*b
else:
  prize=100*((a if a>b else b) if ((a if a>b else b)>c) else c)

print(prize)