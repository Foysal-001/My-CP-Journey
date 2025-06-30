t=int(input())
for j in range(t):
    n=int(input())
    inputs=input()
    a=list(map(int,inputs.split()))
    b=[]
    for i in range(max(a)+1):
        b.append(0)
    for i in range(n) :
        b[a[i]]+=1
    maxf=max(b)
    print(n-maxf)