#new syntax style looks cool
import sys
input=sys.stdin.readline
for i in range(int(input())):
    n,a,b=map(int, input().split())
    s=input()
    x,y=0,0
    for i in range(100):
        for j in range(n):
            if s[j] =='N': y+=1
            elif s[j] == 'S': y-=1
            elif s[j] == 'E': x+=1
            else: x-=1
            if x==a and y==b: flag=True;print('YES');break
            else: flag=False; continue
        if flag==True:break
    if flag==False:print('NO')
    else:continue
