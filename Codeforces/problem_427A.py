n=int(input())
s=list(map(int, input().split()))
sum=0
crime=0
for i in range(len(s)):
    if s[i]>0:
        sum+=s[i]
    else:
        if sum>0:
            sum-=1
        else:
            crime+=1
            
print(crime)
        

