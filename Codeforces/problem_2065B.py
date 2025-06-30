t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b1 = b[0]  # Since m = 1, there's only one element in b
    
    # Perform the operation on each element if beneficial
    for i in range(n):
        if b1 - a[i] < a[i]:  # Only modify if it helps sorting
            a[i] = b1 - a[i]
    
    # Check if the resulting array is non-decreasing
    if sorted(a) == a:
        print("YES")
    else:
        print("NO")
