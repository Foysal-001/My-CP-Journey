for i in range(int(input())):
    n=int(input())
    s=input()
    count=(len(set(s))*2)+(n-len(set(s)))
    print(count)