n=int(input())
mishka=[]
chris=[]
countM=0
countC=0
for i in range(n):
    a,b=map(int, input().split())
    mishka.append(a)
    chris.append(b)

for i in range(n):
    if mishka[i] >chris[i]:
        countM+=1
    elif mishka[i]<chris[i]:
        countC+=1
    else:
        pass

if countM > countC:
    print('Mishka')
elif countM < countC:
    print('Chris')
else:
    print('Friendship is magic!^^')