
 
for i in range(int(input())):
  t = int(input())
  s = list(map(int,input().split()))
 
  a = 0
  b = 0
 
  for i in range(t):
    if i%2 != s[i]%2:
      if i%2 == 0:
        b+=1
      else:
        a+=1
 
  if a == b:
    print(a)
  else:
    print(-1)
 