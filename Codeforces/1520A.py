for i in range(int(input())):
    n=int(input())
    s=input()
    l=[]
    for i in range(n):
        l.append(s[i])

    found=0
    for i in range (1,len(l)):
        if l[i]!=l[i-1] and l[i-1] in l[i+1:]:
            found=1
            break
    print("YES" if found ==0 else "NO")