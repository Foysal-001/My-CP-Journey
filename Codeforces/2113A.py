t = int(input())
for _ in range(t):
    k, a, b, x, y = map(int, input().split())
    gg1 = k
    count1 = 0
    if gg1 >= a:
        cook_a = (gg1 - a) // x + 1
        gg1 -= cook_a * x
        count1 += cook_a

    if gg1 >= b:
        cook_b = (gg1 - b) // y + 1
        count1 += cook_b
    gg2 = k
    count2 = 0
    if gg2 >= b:
        cook_b = (gg2 - b) // y + 1
        gg2 -= cook_b * y
        count2 += cook_b
    if gg2 >= a:
        cook_a = (gg2 - a) // x + 1
        count2 += cook_a
    print(max(count1, count2))
