import sys
input= sys.stdin.readline
a,b=map(int, input().split())
if a==b:
    print('1')
    print(a)

else:
    l=[]
    l.append(b)
    l.append(b)
    l.append(3*a-2*b)
    print('3')
    print(*l)