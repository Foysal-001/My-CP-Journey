for i in range(int(input())):
    s=[0,1,0,3,2,0,2,5]
    a=set(s)
    n=int(input())
    l=list(map(int, input().split()))
    if len(l)>8:
        print(len(l)-1)
    else:
        for i in range(len(l)):
            if l[i]== s[i]:
                del l[i]
            else:
                pass

        if len(s)==len(l):
            print(len(s))
        else:
            print('0')