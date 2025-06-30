'''t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    while len(a) > 1:
        max_sum = 0
        a_i = -1
        a_j = -1
        a_x = -1
        
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j:
                    for x in range(1, 2001):
                        if a[i] + a[j] > x and a[i] + x > a[j] and a[j] + x > a[i]:
                            if x > max_sum:
                                max_sum = x
                                a_i = i
                                a_j = j
                                a_x = x
        
        a.pop(max(a_i, a_j))
        a.pop(min(a_i, a_j))
        a.append(a_x)

    print(a[0)'''
'''def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        return

    results = []
    
    def calculate(arr):
        if len(arr) == 1:
            results.append(arr[0])
            return
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for x in range(1, 2001):
                    if arr[i] + arr[j] > x and arr[i] + x > arr[j] and arr[j] + x > arr[i]:
                        temp_arr = arr[:]
                        val1 = temp_arr.pop(j)
                        val2 = temp_arr.pop(i)
                        temp_arr.append(x)
                        calculate(temp_arr)
                        
    calculate(a)
    print(max(results))


t = int(input())
for _ in range(t):
    solve'''

for i in range(int(input())):
    x = int(input())
    for y in range(1, x):
        xor_val = x ^ y
        if x + y > xor_val and x + xor_val > y and y + xor_val > x:
            print(y)
            break
    if not (x + y > xor_val and x + xor_val > y and y + xor_val > x):
        print('-1')
        
