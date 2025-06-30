t=int(input())
for  i in range(t):
    n,m,k =map(int,input().split())
    a=min(n,k)
    b=min(m,k)
    print(a*b)