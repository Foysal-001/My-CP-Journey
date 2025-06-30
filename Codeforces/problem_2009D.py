from collections import Counter
for _ in range(int(input())):
    n = int(input())
    nums = []
    for i in range(n):
        x,y = map(int,input().split())
        nums.append((x,y))
    ans = 0
    b = Counter(x[0] for x in nums)
    check = set(nums)
    for i in b:
        if b[i]==2: ans += n-2
    for p in check:
        if (p[0]-1,p[1]^1) in check and (p[0]+1,p[1]^1) in check: 
            ans +=1
    print(ans)