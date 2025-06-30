
for i in range(int(input())):
    n, k = map(int, input().split())
    if k == 0:
        print('0' * n)
    elif k == n:
        print('1' * n)
    else:
        res = []
        for i in range(n):
            if i < k:
                res.append('1' if i % 2 == 0 else '0')
            else:
                res.append('0')
        print(''.join(res))