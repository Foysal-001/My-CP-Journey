

x=int(input())
for i in range(x):
  a=input()
  if len(a)>10:
    print(f'{a[0]}{len(a)-2}{a[-1]}')
  else:
    print(a)