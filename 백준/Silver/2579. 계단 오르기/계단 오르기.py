import sys

input = sys.stdin.readline
n = int(input())

dp = [0] * (n + 1)
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

if n >= 1:
    dp[1] = stairs[1]
if n >= 2:
    dp[2] = stairs[1] + stairs[2]
if n >= 3:
    dp[3] = max(stairs[3] + stairs[2], stairs[3]+stairs[1])
if n >= 4:
    for i in range(4,n+1):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+ dp[i-2])

print(dp[n])