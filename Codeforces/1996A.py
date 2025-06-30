for i in range(int(input())):
    n=int(input())
    if n == 2:
        print('1')

    elif n% 4 == 0:
        print(int(n/4))

    else:
        print(int(n/4)+1)