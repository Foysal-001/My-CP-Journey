n=int(input())
for i in range(n):
    m=int(input())
    a=list(map(int,input().split(" ")))
    a.sort()
 
    j=0
    k=1
    if len(a)==1:
        print("YES")
    else:
        while j < len(a):
            if len(a) == 1:
                break
            if k==len(a):
                break
            k=j+1
            while k <= len(a)-1:
 
                if abs(a[j] - a[k]) <= 1:
                    if a[j] < a[k]:
                        a.remove(a[j])
                        break
                    else:
                        a.remove(a[k])
                        break
 
                else:
                    k+=1
 
        if len(a) == 1:
            print("YES")
        else:
            print("NO")