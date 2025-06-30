t=int(input())
for i in range(t):
  s=list(map(int, input().split()))
  if s[0]>s[1] and s[0]>s[2]:
    if s[1]>s[2]:
      print(s[1])
    else:
      print(s[2])
  elif s[0]<s[1] and s[1]>s[2]:
    if s[2]>s[0]:
      print(s[2])
    else:
      print(s[0])
  elif s[2]>s[0] and s[2]>s[1]:
    if s[0]>s[1]:
      print(s[0])
    else:
      print(s[1]) 
