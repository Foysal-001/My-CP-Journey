t = int(input().strip())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    strength_j = a[j-1]
    count_stronger = sum(1 for x in a if x > strength_j)
    if count_stronger == 0:
        print("YES")
    else:
        if k >= 2:
            print("YES")
        else:
            print("NO")
