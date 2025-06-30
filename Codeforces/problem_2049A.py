for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    l=[]
    for k in range(n):
        if s[k]==0:
            pass
        else:
            l.append(s[k])
    
    #count=0
    #gg=0
    if all(x==0 for x in s):
       print('0')
    elif  len(set(l))<len(l) and 0 in s:
       print('2')
    elif len(set(l))==len(l) and s[0]!=0 and 0 in s:
        print('2')
    else:
       print('1')
    























       ''' else:
            gg+=1
        if count==n and gg==0:
            print('0')
            break
        elif count==0 and gg>0:
            print('1')
            break
        elif len(set(l))<len(l) and gg>0:
            print('2')
            break
        elif count>0 and gg>0:
            print('1')
            break
        else:
            pass

'''