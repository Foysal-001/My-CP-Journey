t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    o,e=0,0
    for j in range(l,r+1):
        if j%2!=0:
            o+=1
        else:
            e+=1
    if(o>=2) and  e>=o//2:
        print(o//2)
    else:
        print(0)