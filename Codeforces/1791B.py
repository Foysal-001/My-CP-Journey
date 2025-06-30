for i in range(int(input())):
    n=int(input())
    s=input()
    x,y=0,0
    for i in range(n):
        if s[i] == 'U':
            y+=1
        elif s[i] == 'D':
            y-=1
        elif s[i] == 'R':
            x+=1
        else:
            x-=1
        
        if x == 1 and y == 1:
            print('YES')
            break
        else:
            if i == (n-1):
                print('NO')
                break
            else:
                continue
