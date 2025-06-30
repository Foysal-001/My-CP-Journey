for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    final1=max(a,b)
    final2=max(c,d)
    if final2 > min(a,b) and final1 > min(c,d):
        print('YES')
    else:
        print('NO')
         