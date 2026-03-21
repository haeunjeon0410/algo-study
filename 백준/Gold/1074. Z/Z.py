import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

size = (2**n)
order = 0
half = int((size*size//4) ** 0.5)
while half > 1:
    if n > 1:
        if r > half-1:
            order += ((half*half)*2)
            r -= half
            if c > half-1:
                order += (half*half)
                c -= half

        else:
            if c > half-1:
                order += (half*half)
                c -= half
    half = int((half*half//4) ** 0.5)

order_list = [(0,0), (0,1), (1,0), (1,1)]
for i in range(4):
    if order_list[i] == (r, c):
        print(order+i)
        break
       