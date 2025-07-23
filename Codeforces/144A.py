import sys
input= sys.stdin.readline
n=int(input())
s=list(map(int, input().split()))
maxh=max(s)
minh=min(s)
maxc=s.index(maxh)
minc=n-1-s[::-1].index(minh)
if maxc>minc:
    count=maxc+(n-1-minc)-1
else:
    count=maxc+(n-1-minc)
sys.stdout.write(str(count) + '\n')
