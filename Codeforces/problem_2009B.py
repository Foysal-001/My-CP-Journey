for i in range(int(input())):
    n=int(input())
    l=[input().find('#')+1 for j in range(n)]
    print(*l[::-1])