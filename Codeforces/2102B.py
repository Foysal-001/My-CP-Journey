import sys
import math
input= sys.stdin.readline
for i in range(int((input()))):
    n=int(input())
    s=list(map(int, input().split()))
    if n==1:
        print('YES')
    else:
        s= [abs(i) for i in s]
        l=sorted(s)
        if s[0] <= l[n//2]:
                print('YES')
        else:
                print('NO')
