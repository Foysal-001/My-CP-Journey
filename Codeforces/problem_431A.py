s=list(map(int, input().split()))
t=str(input())
total=0
for i in range(len(t)):
    if t[i]=='1':
        total+=s[0]
    elif t[i]=='2':
        total+=s[1]
    elif t[i]=='3':
        total+=s[2]
    else:
        total+=s[3]
print(total)

