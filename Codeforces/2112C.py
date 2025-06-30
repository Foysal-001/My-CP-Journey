from collections import Counter
from math import comb

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    cnt = Counter(a)
    keys = sorted(cnt)
    for i in range(len(keys)):
        for j in range(i, len(keys)):
            for k in range(j, len(keys)):
                x, y, z = keys[i], keys[j], keys[k]
                s = x + y + z
                if s <= a[-1]:
                    continue
                c = [cnt[x], cnt[y], cnt[z]]
                if x == y == z:
                    if c[0] >= 3:
                        res += comb(c[0], 3)
                elif x == y:
                    if c[0] >= 2 and c[2] >= 1:
                        res += comb(c[0], 2) * c[2]
                elif y == z:
                    if c[1] >= 2 and c[0] >= 1:
                        res += comb(c[1], 2) * c[0]
                elif x == z:
                    if c[0] >= 2 and c[1] >= 1:
                        res += comb(c[0], 2) * c[1]
                else:
                    res += c[0] * c[1] * c[2]
    print(res)
