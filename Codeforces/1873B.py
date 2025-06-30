'''for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    count=min(s)
    res=1
    idx=0
    for j in range(n):
        if s[j] != count:
            res*=s[j]
            idx+=1
        else:
            res*= (s[j] +1)
            idx+=1
            break
    if idx==0:
        idx+=1
    else:
        pass

    for p in range(idx, n):
        res*=s[p]
    if count == 0:
            print(res)
    else:
            print(res)'''

#Optimized one 

for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    mini=min(s)
    if mini == 0:
        mini=1
    prod=1
    for i in range(n):
        prod*=s[i]

    print(int((prod/mini)*(mini)) if mini ==1 else int((prod/mini)*(mini+1)))