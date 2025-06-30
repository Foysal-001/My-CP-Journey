t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        train = dp[i - 1] + a[i - 1]
        if i < n:
            train -= b[i]
        skip = dp[i - 1]
        dp[i] = max(train, skip)
    
    print(dp[n])


