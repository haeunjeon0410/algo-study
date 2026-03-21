import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))

time.sort()
total = 0
new = 0

for i in range(n):
    new += time[i]
    total += new

print(total)

