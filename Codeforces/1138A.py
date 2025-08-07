import sys
input=sys.stdin.readline

n=int(input())
s=list(map(int, input().split()))
blocks = []  
current_type = s[0]
count = 1

for i in range(1, n):
    if s[i] == current_type:
        count += 1
    else:
        blocks.append((current_type, count))
        current_type=s[i]
        count= 1
blocks.append((current_type, count))  
max_len = 0
for i in range(len(blocks) - 1):
    if blocks[i][0] != blocks[i+1][0]:
        max_len = max(max_len, 2 * min(blocks[i][1], blocks[i+1][1]))

print(max_len)

    
    