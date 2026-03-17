import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        q.append(cmd[1])

    elif cmd[0] == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(q))

    elif cmd[0] == 'empty':
        print(0 if q else 1)
        
    elif cmd[0] == 'top':
        if q:
            print(q[-1])
        else:
            print(-1)


