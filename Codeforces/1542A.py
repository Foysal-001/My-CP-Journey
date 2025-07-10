for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    even=0
    odd=0
    for j in range(2*n):
        if s[j] %2 == 0:
            even+=1

        else:
            odd+=1


    if odd == even:
        print('YES')

    else:
        print('NO')
        