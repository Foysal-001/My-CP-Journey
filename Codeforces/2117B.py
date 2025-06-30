import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dq = deque()
    left = True 
    for num in range(n, 0, -1):
        if not dq:
            dq.append(num)
        else:
            if left:
                dq.appendleft(num)
            else:
                dq.append(num)
            left = not left
    print(' '.join(map(str, dq)))
