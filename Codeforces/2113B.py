import sys
input= sys.stdin.readline
for i in range(int(input())):
    x,y,a,b = map(int, input().split())
    x1,y1,x2,y2 = map(int, input().split())
    xx = x1+a
    yy = y1+b
    if x1==x2:
        if (abs(y2-yy))%b:
            print("NO")
        else:
            print("YES")
    elif y1==y2:
        if (abs(x2-xx))%a:
            print("NO")
        else:
            print("YES")
    elif (abs(x2-xx))%a and (abs(y2-y1))%b:
        print("NO")
        
    else:
        print("YES")
    


