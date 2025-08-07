import sys
input = sys.stdin.readline
n=int(input())
l=[]
for p in range(n):
    ll=list(map(int, input().split()))
    l.extend(ll)
xcount=0
for i in range(0,len(l),3):
    xcount+=l[i]

ycount=0
for j in range(1,len(l),3):
    ycount+=l[j]

zcount=0
for k in range(2,len(l),3):
    zcount+=l[k]

if ycount ==0 and zcount ==0 and xcount ==0 :
    print('YES')
else:
    print('NO')

