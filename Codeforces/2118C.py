import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    mx1 = -1  # largest value
    mx2 = -1  # second largest value
    pos = []  # positions of largest value

    for i in range(n):
        for j in range(m):
            v = a[i][j]
            if v > mx1:
                mx2 = mx1
                mx1 = v
                pos = [(i, j)]
            elif v == mx1:
                pos.append((i, j))
            elif v > mx2:
                mx2 = v

    # Since operation decreases all elements in chosen row and column by 1,
    # we can always pick a row and column that includes a cell with the max value.
    # So minimal max after operation is max(mx1 - 1, mx2)
    print(max(mx1 - 1, mx2))
