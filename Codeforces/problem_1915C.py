
import math
for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    #b=sum(a)
    #c=b**(1/2)
    print('YES' if math.isqrt(sum(a))**2==sum(a)  else 'NO')