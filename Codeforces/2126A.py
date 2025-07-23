import sys
input= sys.stdin.readline
for i in range(int(input())):
    x=int(input())
    if x < 10:
        print(x)
    else:
        a=str(x)
        l=[]
        for i in range(len(a)):
            l.append(int(a[i]))

        print(min(l))