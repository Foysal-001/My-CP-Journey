n=int(input())
s=list(map(int, input().split()))
a=1
b=0

for i in range(n-1):
    if s[i] < s[i+1]:
        a+=1

    else:
        if b> a:
            pass
        else:
            b=a
        a=1
        continue

if b> a:
    pass
else:
    b=a

print(b)