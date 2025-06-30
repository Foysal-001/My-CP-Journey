for i in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    total=sum(a)
    flag=True
    for j in range(k):
        if min(a) >= max(b):
            print(total)
            flag= False
            break
            

        elif min(a) < max(b):
            temp= min(a)
            a.remove(temp)
            temp2=max(b)
            b.remove(temp2)
            total= total - temp + temp2
            continue

        else:
            continue
            
        
    if flag:
        print(total)

    else:
        pass

            