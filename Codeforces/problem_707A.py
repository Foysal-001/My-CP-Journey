s=list(map(int, input().split()))
n=list(map(str, input().split()))
m=list(map(str, input().split()))
if 'C' or 'M' or 'Y' in n or m:
    print('#Color')
else:
    print('#Black&White')