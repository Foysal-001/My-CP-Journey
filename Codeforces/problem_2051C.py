for i in range(int(input())):
    n,m,k=map(int, input().split())
    lm=list(map(int, input().split()))
    backup=lm.copy()
    lk=list(map(int, input().split()))
    rs=''
    if m==k:
        print('1'*k)
    elif n>m:
        print('0'*m)
    else:
        for i in range(len(lm)):
            lm.remove(lm[i])
            c=0
            for j in range(k):
                if lm[j]==lk[j]:
                    c+=1
                else:
                    pass
            if c==k:
                rs+='1'
            else:
                rs+='0'
            lm=backup.copy()
        print(rs)
























