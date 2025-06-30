t=int(input())

for i in range(t):
  n=str(input()).split(' ')
  if int(n[0])+int(n[1])== int(n[2]):
    print('YES')
  elif int(n[0])+ int(n[2])== int(n[1]):
    print('YES')
  elif int(n[1])+ int(n[2])== int(n[0]):
    print('YES')
  else:
    print('NO')
