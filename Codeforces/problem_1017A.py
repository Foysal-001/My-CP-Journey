'''
t=int(input())
for i in range(1,t+1):
    n=list(map(int, input().split()))
    if i==1:
        thomas= n[0]+n[1]+n[2]+n[3]
    else:
'''


n=int(input())
l=[]
for i in range(n):
  a,b,c,d=map(int,input().split())
  s=a+b+c+d
  l.append(s)
a1=l[0]
l.sort()
l=l[::-1]
print(l.index(a1)+1)