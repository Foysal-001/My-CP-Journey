'''t=int(input())
for i in range(t):
    s=list(map(int, input().split()))
    if s[0]==1 or s[0]==2:
        print(s[0])
    else:
        print((s[0]//s[1])+1)'''
 
for i in range(int(input())):
    n,x=map(int, input().split())
    if n>2:
        print(((n-3)//x)+2)
    else:
        print(1)

