import sys
input=sys.stdin.readline
for i in range(int(input())):
    n, k = map(int, input().split())
    l = []
    for j in range(n):
        li, ri, reali = map(int, input().split())
        l.append([li, ri, reali, False])  
    while True:
        idx = -1     
        earn = k  
        for i in range(n):
            li, ri, reali, spend = l[i]
            if not spend and li <=k<=ri:   
                if reali>earn:
                    earn=reali
                    idx=i
        if idx==-1:
            break
        k=earn
        l[idx][3]=True  
    print(k)