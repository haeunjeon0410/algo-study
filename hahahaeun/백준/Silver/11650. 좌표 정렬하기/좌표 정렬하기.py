import sys
input = sys.stdin.readline

n = int(input())
point = []

for _ in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

sorted_point = sorted(point, key=lambda x: (x[0], x[1]))

for i in sorted_point:
    print(*i)