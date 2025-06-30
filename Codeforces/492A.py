n=int(input())
count=0
res=0
while True:
    count+=1
    res+= (count*(count+1))/(2)
    if res==n:
        print(count)
        break

    elif res >= n:
        if count==1:
            print(count)
            break
        else:
            print(count-1)
        break
    else:
        continue
