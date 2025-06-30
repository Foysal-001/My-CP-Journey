a,b=map(int,input().split())
count=1
while True:
    if (count*a)%10!=0:
        c=(count*a)
        d=c-b
        if d%10==0:
            print(count)
            break
        else:
            count+=1
    else:
        print(count)
        break