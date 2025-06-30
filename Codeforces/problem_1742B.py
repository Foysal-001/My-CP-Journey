for i in range(int(input())):
    a=int(input())
    n=list(map(int, input().split()))
    if len(n) == len(set(n)):
        print('YES')
    else:
        print('NO')
        