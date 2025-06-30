for i in range(int(input())):
    n=int(input())
    s=str(input())
    count= len(set(s))
    print((count*2) if n == count else ((count*2)+(count-1)) )
    