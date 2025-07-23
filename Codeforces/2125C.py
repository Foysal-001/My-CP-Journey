'''import sys
import math
input= sys.stdin.readline
for i in range(int(input())):
    def prime_factors(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 1:
            factors.append(n)
        return factors
    l,r=map(int, input().split())
    count=0
    for j in range(l, r+1):
        if j %2 ==0 or j%3==0 or j%5==0 or j%7==0:
            continue
        else:
            ll=prime_factors(j)
            for k in range(len(ll)):
                if ll[k]>10:
                    gg=True
                else:
                    gg=False
                    break
            if gg==True:
                count+=1
            else:
                continue
    print(count)'''

import sys
input=sys.stdin.readline
for i in range(int(input())):
    l,r=map(int, input().split())
    count=r-l+1
    kharap=0
    ll=[2,3,5,7]
    for j in range(1,1<<4):  
        a=1
        b=0
        for i in range(4):
            if (j>>i) & 1:
                a*=ll[i]
                b+=1
        c=r//a-(l-1)//a
        if b%2==1:kharap+=c   
        else:kharap-=c        
    print(count-kharap)


