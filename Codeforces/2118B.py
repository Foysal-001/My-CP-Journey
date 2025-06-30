t = int(input())
for _ in range(t):
    n = int(input())
    ops = []
    
    if n == 3:
        ops = [(2,1,3), (2,2,3), (3,1,2), (3,2,3)]
    elif n == 4:
        ops = [(2,1,4), (3,1,3), (3,2,4), (4,3,4), (4,1,2)]
    else:
        # General case
        ops.append((2, 1, n))
        for i in range(3, n):
            ops.append((i, 1, n - i + 2))
            ops.append((i, i - 1, n))
        ops.append((n, 1, n - 1))
        ops.append((n, 2, n))
    
    # Filter valid operations
    ops = [op for op in ops if op[1] <= op[2]]
    
    print(len(ops))
    for op in ops:
        print(op[0], op[1], op[2])