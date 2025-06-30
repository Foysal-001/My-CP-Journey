
'''
s=int(input())
p=list(map(int, input().split()))
p.sort()
count=0
if len(p)==1:
    print('NO')
elif len(p)==2 and p[0]==p[1]:
    print('NO')
    
elif len(p)>2:
    for i in range((len(p)+1)):
        if p[i]==p[i+1] and i<len(p):
            count+=1
        elif count==len(p)-1:
            print('NO')      
        else:
            print(p[i+1])
            break

    #if count==len(p)-1:
     #   print('NO')


'''    
input()
n= sorted(set(map(int,input().split())))
print(n[1] if len(n)>1 else "NO")