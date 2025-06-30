'''for i in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    one= l.count(1)
    two= l.count(2)
    if sum(l)% 2 != 0:
        print('NO')
    else:

        if one==0:
            if two %2 ==0 :
                print('YES')

            if two %2 != 0:
                 print('NO')


        elif one == 2:
                print('YES')

        else:
                half= int(sum(l) /2 )
                l.sort()
                total=0
                for i in range(len(l)):
                    total+=l[i]
                    if total == half:
                        print('YES')
                        break
                    elif total > half :
                        print('NO')
                        break
                    else:
                         continue'''
#Correct one 
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    total = sum(l)
    
    if total % 2 != 0:
        print("NO")
    else:
        one = l.count(1)
        two = l.count(2)
        half = total // 2
        found = False
        for j in range(two + 1):
            total = j * 2
            rem = half - total
            if rem >= 0 and rem <= one:
                found = True
                break  
        print("YES" if found else "NO")
