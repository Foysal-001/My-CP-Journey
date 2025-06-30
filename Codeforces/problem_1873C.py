t=int(input())
for h in range(t):
    point=0
    a=[input() for i in range(10)]
    for i in range(10):
        for j in range(10):
            if a[i][j]=='X':
                point+=min(10-i,i+1,j+1,10-j)
    print(point)