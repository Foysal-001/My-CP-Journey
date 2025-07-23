import sys
input=sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    l=[]
    for i in range(n):
        if a[i]>b[i]:
            a[i],b[i]=b[i],a[i]
            l.append((3,i+1))
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                l.append((1,j+1))
    for i in range(n):
        for j in range(n-1):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                l.append((2,j+1))
    print(len(l))
    for i in l:
        print(*i)
