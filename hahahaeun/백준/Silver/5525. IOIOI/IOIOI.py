import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

pn = 'I' + 'OI' * n
pn_count = 0

for i in range(m):
    if pn in s[i:len(pn)+i]:
        pn_count += 1

print(pn_count)