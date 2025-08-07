import sys
import math
input=sys.stdin.readline
n=int(input())
if n%2==0:
    print(int((n**2)/2))
    for i in range(1, n+1):
        s=''
        if i %2!=0:
            for j in range(1, n+1):
                if j%2!=0:
                    s+='C'

                else:
                    s+='.'
        else:
            for j in range(1, n+1):
                if j%2!=0:
                    s+='.'
                else:
                    s+='C'
        print(s)
else:
    print((n*(n//2))+math.ceil(n/2))
    for i in range(1, n+1):
        s=''
        if i%2 !=0:
            for j in range(1, n+1):
                if j%2 !=0:
                    s+='C'

                else:
                    s+='.'
        else:
            for j in range(1, n+1):
                if j%2 !=0:
                    s+='.'
                else:
                    s+='C'
        print(s)

