n,k=map(int, input().split())
l=list(map(int, input().split()))
count=0
for i in range(len(l)):
    if (l[i]>l[k-1] or l[i]==l[k-1]) and l[i]>0:
        count+=1
    else:
        pass
print(count)