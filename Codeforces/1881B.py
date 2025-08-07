import sys
input=sys.stdin.readline
for i in range(int(input())):
    a,b,c=map(int, input().split())
    maxi= max(a,b,c)
    mini= min(a,b,c)
    midi= a+b+c - maxi-mini
    if a==b==c:
            print('YES')
        
    elif maxi %mini !=0 or  midi %mini !=0:
            print('NO')

    else:
        if ((maxi/mini)-1 + (midi/mini)-1) <= 3:
            print('YES')

        else:
            print('NO') 
