#After seeing editorial
for i in range(0, int(input())):
    n = int(input())
    one = n // 3
    two = one
    if n % 3 == 1:
        one += 1
    elif n % 3 == 2:
        two += 1
    print(one, two)