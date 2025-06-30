for i in range(int(input())):
    a,b=map(str, input().split())
    m=b[0]+a[1]+a[2]
    n=a[0]+b[1]+b[2]
    print(f'{m} {n}')