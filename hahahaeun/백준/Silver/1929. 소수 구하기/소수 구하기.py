import sys
input = sys.stdin.readline

m, n = map(int, input().split())

num = [True] * (n+1)
num[0] = num[1] = False

for i in range(2, int(n**0.5)+1):
    if num[i]:
        for j in range(i*i, n+1, i):
            num[j] = False

result =[str(i) for i in range(m, n+1) if num[i]]
print("\n".join(result))
