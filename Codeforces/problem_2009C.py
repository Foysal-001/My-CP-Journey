t=int(input())
for i in range(t):
    x,y,k=map(int,input().split())
    a=(x-1)//k+1
    b=(y-1)//k+1
    if a>b:print(2*a-1)
    else:print(2*b)