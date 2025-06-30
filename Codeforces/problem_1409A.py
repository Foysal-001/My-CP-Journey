for i in range(int(input())):
    a,b=map(int, input().split())
    count=0
    if a==b:
        print('0')
    else:
        
        if a > b:
            count=(a-b)//10
            if (a-b)%10 != 0:
                count+=1 
                
        elif a == b:
            pass
            #print('0')
            #break
           
            
        else:
            count=(b-a)//10
            if (b-a)%10 != 0:
                count+=1 
            
        print(count)
    