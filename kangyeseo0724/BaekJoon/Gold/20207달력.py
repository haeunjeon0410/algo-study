import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    day = [0] * 367
    for _ in range(n):
        s, e = map(int, input().split())
        for i in range(s, e + 1):
            day[i] += 1
            
    total_area = 0
    row = 0
    col = 0
    for i in range(1, 367):
        if day[i] > 0:
            row = max(row, day[i])
            col += 1
        else:
            total_area += row * col
            row = 0
            col = 0
    print(total_area)

solve()