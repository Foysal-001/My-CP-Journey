t=int(input())
for i in range(t):
    s=input()
    if s=='abc':
        print('YES')
    else:
        if s[0]=='a' and s[1]=='c' and s[2]=='b':
            print('YES')
        elif s[0]=='c' and s[1]=='b' and s[2]=='a':
            print('YES')
        elif s[0]=='b' and s[1]=='a' and s[2]=='c':
            print('YES')
        else:
            print('NO')