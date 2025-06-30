
t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a= list(map(int, input().split()))
    mv=max(a)
    for j in range(m):
        op, x, y = map(str, input().split())
        x=int(x)
        y=int(y)
 
        if x <= mv and y >= mv:
            if op=='+':
                mv+=1
            else:
                mv-=1
        print(mv,end=" ")
    print()
 