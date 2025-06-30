'''for i in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    one = a.count(1)
    if x > one:
        print('YES')
    elif x < one:
        print('NO')
    else:
        cd = [i for i in range(n) if a[i] == 1]
        gg = cd[0]
        l = cd[-1]
        if (l - gg + 1) <= x:
            print('YES')
        else:
            print('NO')'''
    

#Correct one
for i in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ml = -1
    mr = float('inf')
    for i in range(n):
        if a[i] == 1:
            l = (i + 1) - x + 1
            r = i + 1
            if l > ml:
                ml = l
            if r < mr:
                mr = r
    if ml <= mr:
        print("YES")
    else:
        print("NO")