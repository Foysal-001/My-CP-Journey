for _ in range(int(input())):
    t = int(input())
    a = list(map(int, input().split(' ')))
    
    pair = []
    unpair = []
    res = 0
    
    if(t == 1):
        print(a[0])
    elif(t == 2):
        print(a[0] - a[1])
    else:
        for index, number in enumerate(a):
            if index%2 > 0:
                pair.append(number)
            else:
                unpair.append(number)
        
        
        res = sum(unpair) - sum(pair)
        
        print(res)