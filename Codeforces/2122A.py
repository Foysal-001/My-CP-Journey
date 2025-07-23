import sys
input=sys.stdin.readline
for i in range(int(input())):
    n,m=map(int, input().split())
    if (n>=2 and m>=3) or (n >= 3 and m >= 2):
        print("YES")
    else:
        print("NO")