for i in range(int(input())):
    n=int(input())
    if(n%2==0):
        print(-1)
    else:
        m=n-(n//2)
        l=list(range(m, 0, -1))
        l+=list(range(m+1, n+1))
        print(*l)