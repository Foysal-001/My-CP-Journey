for i in range(int(input())):
    n,k=map(int, input().split())
    s=input()
    if s.count('1') <= k:
        print('Alice')

    elif s.count('1') > k and n >= 2*k:
        print('Bob')

    else:
        print('Alice')
