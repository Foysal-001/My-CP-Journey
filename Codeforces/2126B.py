import sys
input = sys.stdin.readline
for i in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    count=0
    i=0
    while i <= n-k:
        noice=True
        for j in range(i,i+k):
            if a[j]!=0:
                noice=False
                break     
        if noice:
            count+=1
            i+=k+1  
        else:
            i+=1
    print(count)
