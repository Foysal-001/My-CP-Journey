for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(n):
        for j in range(i+1, n):
            b.append(a[j]-a[i])
    print(min(b))
