
def check_prime(num):
    mul=int(num**(1/2))+1
    c=0
    for i in range(2, mul+1):
        if num%i==0:
            c+=1     
        else:
            continue
    if c>0:
        return False
    else:
        return True
    


n,m=map(int,input().split())
while True:
    n+=1
    if check_prime(n)==True:
        if n==m:
            print('YES')
            break
        else:
            print('NO')
            break
    else:
        continue

