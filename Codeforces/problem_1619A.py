for i in range(int(input())):
    n=input()
    s=len(n)//2
    if n[:s]==n[s:]:
        print("YES")
    else:
        print("NO")
            