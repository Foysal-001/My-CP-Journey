for i in range(int(input())):
    p=int(input())
    n=list(map(int, input().split()))
    for j in range(p):
        if n.count(n[j])==1:
            print(j+1)
            break
        else:
            pass