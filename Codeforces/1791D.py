'''for i in range(int(input())):
    n=int(input())
    s=input()
    count=len(set(s))
    if count==1:
        print('2')

    elif count == n:
        print(count)
    
    else:
        a=[]
        b=[]
        c=0
        for i in range(n):
            if s[i] not in a: 
                a.append(s[i])
                c+=1

            else:
                for i in range(n-len(a)):
                    b.append(s[i+c])

                break
        print(len(set(a))+ len(set(b)))'''

for i in range(int(input())):
    n = int(input())
    s = input()
    count = len(set(s))
    
    if count == 1:
        print('2')
    
    elif count == n:
        print(count)
    
    else:
        a = []
        b = []
        c = 0
        for i in range(n):
            if s[i] not in a: 
                a.append(s[i])
                c += 1
            else:
                for i in range(n - len(a)):
                    b.append(s[i + c])
                break
        res = len(set(a)) + len(set(b))
        pre = set()
        val = 0
        for i in range(n - 1):
            pre.add(s[i])
            post = set(s[i + 1:])
            val = max(val, len(pre) + len(post))
        
        print(max(res, val))
