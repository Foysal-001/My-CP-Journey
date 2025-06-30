for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    total=sum(s)
    print('NO' if total%2==0 else 'YES')