
t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    d=b-a
    print(int((1+(1+8*d)**0.5)/2))