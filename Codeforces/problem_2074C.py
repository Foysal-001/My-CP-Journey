'''for i in range(int(input())):
    n=int(input())
    for y in range(1,n):
        xor=n**y
        if n+y>xor and n+xor>y and y+xor>n:
            print(y)
            break
        else:
            print('-1')
            break
def find_y(x):
    y = x - 1
    xor = x ^ y
    if x + y > xor and x + xor > y and y + xor > x:
        return y
    return -1

t = int(input())
for _ in range(t):
    x = int(input())
    result = find_y(x)
    print(result)'''

'''def solve():
  x = int(input())
  if x % 2 == 0:
    print(x - 1)
  else:
    print(-1)

t = int(input())
for _ in range(t):
  solve()'''

'''t = int(input())
for _ in range(t):
    x = int(input())
    found = False
    for y in range(1, x):
        xor_val = x ^ y
        if x + y > xor_val and x + xor_val > y and y + xor_val > x:
            print(y)
            found = True
            break
    if not found:
        print(-1)'''



for i in range(int(input())):
    x = int(input())
    for y in range(1, x):
        xor_val = x ^ y
        if x + y > xor_val and x + xor_val > y and y + xor_val > x:
            print(y)
            break
        else:
         print('-1')
         break
    