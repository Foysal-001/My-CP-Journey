t = int(input())
for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    # The position on the grid the two tiles belong to
    gx1 = (x1 % a + a) % a
    gy1 = (y1 % b + b) % b
    gx2 = (x2 % a + a) % a
    gy2 = (y2 % b + b) % b

    # They must align on the same grid
    if gx1 != gx2 or gy1 != gy2:
        print("No")
    else:
        print("Yes")
