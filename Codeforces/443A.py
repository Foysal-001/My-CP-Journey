n=input().strip()
if len(set(n))-4==-2:
    print('0')
elif len(set(n))-4 <0:
    print('1')
else:
    print(len(set(n))-4)