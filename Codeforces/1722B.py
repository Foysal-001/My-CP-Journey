for i in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    count=0
    for i in range(n):
        if (a[i] == 'R' and b[i] != 'R') or (b[i] == 'R' and a[i] != 'R'):
            print('NO')
            break

        elif a[i] == b[i] or (a[i]== 'G' and b[i] == 'B') or (a[i]=='B' and b[i]=='G') :
            count+=1

        else:
            continue

    if count == n:
        print('YES')

