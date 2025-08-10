import sys
import math
input=sys.stdin.readline
for i in range(int(input())):
    a,b=map(int, input().split())
    gg=math.gcd(a,b)
    print(int((a*b)/gg))
