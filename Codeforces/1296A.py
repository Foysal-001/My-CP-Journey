for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    if sum(s) %2 != 0:
        print('YES')

    else:
        eve=0
        odd=0
        for i in range(n):
            if s[i] %2 == 0:
                eve+=1

            else:
                odd+=1

        if eve >=1 and odd >= 1:
            
            print('YES')

        else:
            print('NO')