import sys
input=sys.stdin.readline
for i in range(int(input())):
	s=input()
	p=0
	q=0
	for c in s:
		if c=='(': 
			q+=1
		else: 
			q-=1
		if q==0: 
			p+=1
	print( "YES" if p >= 2 else "NO" )

			
        