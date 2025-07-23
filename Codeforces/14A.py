import sys
input= sys.stdin.readline
n,c=map(int, input().split())
s=list(map(int, input().split()))
gg=min(s)
g=max(s)
print(g-c-gg)
