t=int(input())
for i in range(t):
    n,m=map(int, input().split())
    if n%2==1  or (n==0 and m%2==1): print('NO')
    else: print('YES')