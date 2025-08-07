import sys
import math
input = sys.stdin.readline
n,m=map(int, input().split())
l=[]
ll=0
for i in range(n):
    a=input()
    l.extend(a)
    aa=a.count('*')
    if aa>ll:
        ll=aa
    else:
        continue

print(ll)


