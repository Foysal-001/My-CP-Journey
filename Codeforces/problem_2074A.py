'''for i in range(int(input())):
    s=list(map(int,input().split()))
    if s[0]==s[1]==s[2]==s[3]:
        print('YES')
    else:
        print('NO')'''
        


for i in range(int(input())):
    s=list(map(int, input().split()))
    print('YES' if len(set(s))==1 else 'NO')