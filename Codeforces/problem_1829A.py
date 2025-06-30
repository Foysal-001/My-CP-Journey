t=int(input())
c='codeforces'
for i in range(t):
    s=input()
    count=0
    for i in range(10):
        if s[i]==c[i]:
            pass
        else:
            count+=1
    print(count)

