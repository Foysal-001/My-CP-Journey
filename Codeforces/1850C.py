for i in range(int(input())):
    l=''
    for j in range(8):
        x= input()
        for _ in range(8):
            if x[_] != '.':
                l+=x[_]
            else:
                continue
    print(l)