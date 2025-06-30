t=int(input())
for i in range(t):
    l=[]
    count=0
    n=int(input())
    s=list(map(int, input().split()))
    for j in range(len(s)):
        if s[j]==0:
            count+=1
            l.append(count)
        else:
            l.append(count)
            count=0
    if len(l)==0 or max(l)==0:
        print(count)
    else:
        print(max(l))
    
