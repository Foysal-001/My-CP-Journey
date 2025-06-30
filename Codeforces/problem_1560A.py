liked_numbers = []
i = 1
while len(liked_numbers) < 1000:  
    if i % 3 != 0 and i % 10 != 3:
        liked_numbers.append(i)
    i += 1
 
t = int(input())
results = []
for _ in range(t):
    k = int(input())
    results.append(liked_numbers[k - 1])  
 
for result in results:
    print(result)