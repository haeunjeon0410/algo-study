import sys
from collections import deque
input = sys.stdin.readline

n = list(input().strip())
n_sum = 0
for i in range(len(n)):
    if n[i] != '*':
        if (i+1) % 2 != 0:
            n_sum += int(n[i])

        else:
            n_sum += (3 * int(n[i]))
    else:
        position = i

for i in range(10):
    if (position+1) % 2 != 0:
        if (i+n_sum) % 10 == 0:
            print(i)
            break
    else:
        if (3*i+n_sum) % 10 == 0:
            print(i)
            break

