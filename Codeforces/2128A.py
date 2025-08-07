for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    res = n
    for k in range(n + 1):
        cnt = 0
        ok = True
        for i in range(n):
            t = max(0, i - k)  # how many times it has doubled
            w = a[i] * (1 << t)
            if w > c:
                cnt += 1
        res = min(res, cnt)
    print(res)
