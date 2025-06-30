for i in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    count=int(sum(l)/n)
    give=0
    receive=0
    for i in range(n):
        if l[i] >= count:
            give+=(l[i])-count
            if give - receive >=0 :
                continue 
            else:
                print('NO')
                break
        elif l[i] < count:
            receive+=count-l[i]
            if give - receive >= 0:
                continue 
            else:
                print('NO')
                break
    if give == receive :
        print('YES')
        
