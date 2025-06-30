t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n % 2 == 0:
        print(-1)
    else:
        perm = []
        for i in range(1, n + 1, 2):
            perm.append(i)
        for i in range(2, n + 1, 2):
            perm.append(i)
        print(*perm)