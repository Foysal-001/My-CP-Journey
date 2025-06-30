t=int(input())
f=str(input()).lower()
if len(f)!=t:
  print("NO")
elif len(set(f))==26:
  print('YES')
else:
  print("NO")
