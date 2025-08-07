import sys
input=sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    if len(set(a)) == n and n>1:
        print('YES')
    else:
        print('NO')
        