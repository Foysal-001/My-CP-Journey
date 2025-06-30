for i in range(int(input())):
    a,b,c=map(int, input().split())
    if (a+b+c)%3!=0:
        print('No')
    else:
        if a> (a+b+c)/3 or b> (a+b+c)/3:
            print('NO')
        else:
            print('YES')
        