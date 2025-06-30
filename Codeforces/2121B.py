for i in range(int(input())):
    n = int(input())
    s = input().strip()
    lp = [False] * n
    pre = [False] * 50
    for i in range(n):
        if i > 0:
            lp[i] = pre[ord(s[i]) - ord('a')]
        pre[ord(s[i]) - ord('a')] = True
    sp = [False] * n
    suf = [False] * 50
    for i in range(n-1, -1, -1):
        if i < n-1:
            sp[i] = suf[ord(s[i]) - ord('a')]
        suf[ord(s[i]) - ord('a')] = True
    got = False
    for i in range(1, n-1):
        if lp[i] or sp[i]:
            got = True
            break
    print("YES" if got else "NO")
