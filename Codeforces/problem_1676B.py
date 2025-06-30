for i in range(int(input())):
    n=int(input())
    s=list(map(int, input().split()))
    a=min(s)
    count=0
    for i in range(len(s)):
        if s[i]==a:
            count+=0
        else:
            count+=(s[i]-a)
    print(count)