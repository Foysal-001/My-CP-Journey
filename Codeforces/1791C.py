for i in range(int(input())):
    n=int(input())
    s=input()
    l=[]
    for j in range(len(s)):
        l.append(s[j])

    while True:

        if len(l) == 0:
            print('0')
            break
        
        if l[-1] == l[0]:
            print(len(l))
            break
        else:
            del l[-1]
            del l[0]

