for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=1  
    for i in range(n):
        a=l[i]-2*i
        if a<=0:
            x=0
    for i in range(n-1,-1,-1):
        a=l[i]-2*(n-(i+1))
        if a<=0:
            x=0
    if x:
        print('YES')
    else:
        print('NO')