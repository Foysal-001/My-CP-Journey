n1=str(input())
n2=str(input())
n3=str(input())
l1=[]
l2=[]
l3=[]
for _ in range(len(n1)):
  l1.append(n1[_])
for _ in range(len(n2)):
  l2.append(n2[_])
for _ in range(len(n3)):
  l3.append(n3[_])

if len(n1)+len(n2)!=len(n3):
  print('NO')
else:
  for j in range(len(n1)):
    if n1[j] in l3:
        l3.remove(n1[j])
    else:
      break
  for q in range(len(n2)):
    if n2[q] in l3:
        l3.remove(n2[q])
    else:
      break
  if len(l3)==0:
    print("YES")
  else:
    print('NO')