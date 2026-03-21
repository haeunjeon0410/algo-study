import sys
input = sys.stdin.readline

m, n = map(int, input().split())

num = []

for i in range(m, n+1):
    prime = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            prime = 0
            break

    if prime:
        if i != 1:            
            num.append(i)

for x in num:
    print(x)