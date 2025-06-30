n=int(input())
s=list(map(int,input().split()))
count=0
for i in range(1,n):
    if s[i]>max(s[:i]) or s[i]<min(s[:i]):
        count+=1
print(count)
