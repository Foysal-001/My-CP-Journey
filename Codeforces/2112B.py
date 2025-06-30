t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ok = False
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            ok = True
            break
    if ok:
        print(0)
    elif n == 2:
        print(-1)
    else:
        print(1)
