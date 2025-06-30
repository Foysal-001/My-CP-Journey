t=int(input())
for i in range(t):
    s=input()
    p,r,q=int(s[0]), str(s[1]) , int(s[2])
    if p>q and p!=q:
        print(f'{p}>{q}')
    elif q>p and p!=q:
        print(f'{q}>{p}')
    else:
        print(f'{p}={q}')
