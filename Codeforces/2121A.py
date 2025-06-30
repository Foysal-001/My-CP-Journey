t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    min_x = min(x)
    max_x = max(x)
    if s <= min_x:
        steps = max_x - s
    elif s >= max_x:
        steps = s - min_x
    else:
        steps = (max_x - min_x) + min(s - min_x, max_x - s)
    print(steps)