for i in range(int(input())):
    n,a,b=map(int, input().split())
    if n%2 == 0:
        if int((n/2)*b) < n*a:
            print(int((n/2)*b))
        else:
            print(n*a)
    else:
        if int((n//2)*b + a) < n*a:
            print(int((n//2)*b + a))
        else:
            print(n*a)