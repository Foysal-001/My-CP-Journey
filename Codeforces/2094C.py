import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    diag = {}  # i+j (1-based) -> value of p[i+j]

    for i in range(n):
        for j in range(n):
            k = i + j + 2  # i and j are 0-based, so i+j+2 is 1-based (starts from 2)
            if k not in diag:
                diag[k] = a[i][j]

    res = []
    for i in range(2, 2 * n + 1):
        res.append(diag[i])
    
    print(*res)

