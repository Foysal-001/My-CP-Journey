def solution():
    n = int(input())
    s = input()
    m = int(n**0.5)
    return "Yes" if m*m == n and s.count('1') == 4*m-4 else "No"
 
for _ in range(int(input())):
    print(solution())