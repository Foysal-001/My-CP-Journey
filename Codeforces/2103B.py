import sys
input= sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    s=input()
    count=0
    for j in range(n-1):
        if s[j] != s[j+1]:
            count+=1 
    if count == 0:
        if s[0] == '1':
            print(n+1)
        else:
            print(n)
    elif count ==1:
        print(n+1)
    
    else:
        if s[0] == '0' and count >2:
            print(n+count-2)
        else:
            print(n+count-1)