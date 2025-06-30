#for i in range(int(input())):
count=1
s1=str(input())
s2=str(input())
for i in range(len(s2)):
    if s2[i]==s1[count-1]:
        count+=1
    else:
        pass
print(count)
               
