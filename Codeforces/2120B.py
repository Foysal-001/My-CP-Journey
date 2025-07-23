import sys
input= sys.stdin.readline
for i in range(int(input())):
    l1,b1,l2,b2,l3,b3= map(int, input().split())
    if l1+l2+l3 == b1 and b1==b2 and b2==b3:
        print('YES')
    elif (l2+l3 == l1 and b2==b3 and b1+b2==l1):
        print('YES')
    elif (b1+b2+b3 == l1 and l1==l2 and l2==l3):
        print('YES')
    elif (b2+b3 == b1 and l2==l3 and l1+l2==b1):   
        print('YES')
    else:
        print('NO')
