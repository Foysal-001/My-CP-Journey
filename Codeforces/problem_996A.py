n = int(input())
a = n//100
 
b = (n%100)//20
c = ((n%100)%20)//10
d = (((n%100)%20)%10)//5
e = (((n%100)%20)%10)%5
f = a+b+c+d+e
print(f)