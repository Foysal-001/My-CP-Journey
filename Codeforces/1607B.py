import sys
input=sys.stdin.readline
for i in range(int(input())):
    x,n=map(int, input().split())
    if x==0:
        if n%4 ==1:print(-n)
        elif n%4 == 2:print(1)
        elif n%4 == 3:print(n+1)
        else:print(0)
    elif x%2==0:
        if n%4 ==1:print(x-n)
        elif n%4 == 2:print(x+1)
        elif n%4 == 3:print(x+n+1)
        else:print(x+0)
    else:
        if n%4 ==1:print(x+n)
        elif n%4 == 2:print(x-1)
        elif n%4 == 3:print(x-n-1)
        else:print(x-0)