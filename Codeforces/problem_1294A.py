t=int(input())
for i in range(t):
    a,b,c,n=map(int,input().split())
    d=n-max(a,b,c)*3+a+b+c
    if d>=0 and d%3==0:
        print("YES")
    else:
        print("NO")