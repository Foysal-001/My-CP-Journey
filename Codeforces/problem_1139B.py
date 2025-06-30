n=int(input())
l=list(map(int, input().split()))
total = 0
last = float('inf')  
for i in range(n - 1, -1, -1):
        last = min(last - 1, l[i])  
        if last <= 0:  
            break
        total += last  
    
print(total)