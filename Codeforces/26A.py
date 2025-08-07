
import sys
import math
input= sys.stdin.readline
n = int(input())
count = 0
for i in range(1, n + 1):
    x = i
    ll = set()
    while x % 2 == 0:
        ll.add(2)
        x//=2
    j=3
    while j**2 <=x:
        while x % j==0:
            ll.add(j)
            x//=j
        j+=2
    if x>2:
        ll.add(x)
    if len(ll)==2:
        count+=1
print(count)
