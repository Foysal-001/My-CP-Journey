import sys
input=sys.stdin.readline
for i in range(int(input())):
	n=int(input())
	s=input()
	print(s.count('1')*(len(s)-2)+len(s))