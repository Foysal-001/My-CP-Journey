'''for i in range(int(input())):
    n,a,b,c=map(int, input().split())
    count=0
    if n==a or n<a:
        print('1')
    elif a==b and b==c and c==a:
        print(n)
    '''
x = int(input())
for _ in range(x):
    n, p, q, r = map(int, input().split())
    cycle_sum = p + q + r
    full_cycles = n // cycle_sum
    rem = n % cycle_sum

    days = full_cycles * 3
    if rem > 0:
        days += 1
        if rem > p:
            days += 1
            if rem > p + q:
                days += 1
    
    print(days)