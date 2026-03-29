import sys

input = sys.stdin.readline

n = int(input())
pillars = []
max_h = 0
max_idx = 0

for _ in range(n):
    l, h = map(int, input().split())
    pillars.append((l, h))
    if h > max_h:
        max_h = h

pillars.sort()

for i in range(n):
    if pillars[i][1] == max_h:
        max_idx = i

total_area = 0

curr_h = 0
for i in range(max_idx + 1):
    if pillars[i][1] > curr_h:
        curr_h = pillars[i][1]
    
    if i < max_idx:
        total_area += curr_h * (pillars[i+1][0] - pillars[i][0])

curr_h = 0
for i in range(n - 1, max_idx - 1, -1):
    if pillars[i][1] > curr_h:
        curr_h = pillars[i][1]
    
    if i > max_idx:
        total_area += curr_h * (pillars[i][0] - pillars[i-1][0])

total_area += max_h

print(total_area)