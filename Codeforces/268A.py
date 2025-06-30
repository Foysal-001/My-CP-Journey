n = int(input())
a= []
b= []
count = 0
 
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x[0])
    b.append(x[1])
 
for x in a:
    count += b.count(x)
 
print(count)