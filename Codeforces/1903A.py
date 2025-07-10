for i in range(int(input())):
    n,k=map(int, input().split())
    s=list(map(int, input().split()))
    if k==1 and len(set(s)) == 1:
        print('YES')
    elif k==1:
        print('NO')


    else:
         if n-k == 1:
             print('YES')
         elif n == k:
             print('YES')

             
         else:
             print('NO')


