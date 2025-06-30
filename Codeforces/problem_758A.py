t=int(input())
n=list(map(int, input().split()))
if t==1:
    print('0')
else:
    s=sum(n)
    m=max(n)
    total=m*t
    res=total-s
    print(res)