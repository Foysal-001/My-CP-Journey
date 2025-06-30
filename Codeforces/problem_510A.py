l = list(map(int, input().split()))
m = "#"
n = "."
x = l[1]
for i in range(0, l[0]//2):
    if i % 2 == 0:
        print(x*m)
        print((x-1)*n, m, sep='')
    elif i % 2 != 0:
        print(x*m)
        print("#", (x-1)*n, sep='')
    if i == (l[0]//2)-1:
        print(x*m)