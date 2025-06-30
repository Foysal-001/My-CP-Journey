for i in range(int(input())):
    a=str(input())
    

    if len(a)==2:
        print('i')
    else:
        ab=[]
        for j in range(len(a)-2):
            ab.append(a[j])
        b=''
        for p in range(len(ab)):
           b+=ab[p]
        print(b+'i') 
        

