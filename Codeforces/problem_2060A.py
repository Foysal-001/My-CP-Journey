t = int(input().strip())
results = []
for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    a3= [a1 + a2, a4 - a2, a5 - a4]
    max_fib = 0
    for i in a3:
        count = 0
        if a2 + i == a4:
            count += 1
        if i + a4 == a5:
            count += 1
        if a1 + a2 == i:
            count += 1
        max_fib = max(max_fib, count)
    results.append(str(max_fib))
print("\n".join(results))
