for _ in range(int(input())):
	n=int(input())
	i=1
	l=[]
	while n!=0:
		if n%10!=0:
			l.append(int(n%10*i))
		n=n//10
		i*=10
	print(len(l))
	print(*l) 