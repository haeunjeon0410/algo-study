import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

s = input().strip()

pn = 'I' + 'OI' * n
pn_count = 0
size = 2*n+1

for i in range(m):
    if pn in s[i:size+i]:
        pn_count += 1

print(pn_count)