import sys
input= sys.stdin.readline
for i in range(int(input())):
    n,d=map(int, input().split())
    num= int(str(d)*n)
    res=[]
    if num %1 == 0:
        res.append(1)

    if num % 3== 0:
        res.append(3)
    if num % 5 ==0:
        res.append(5)
    if num%7 == 0:
        res.append(7)
    if num%9==0:
        res.append(9)

    print(*res)
    