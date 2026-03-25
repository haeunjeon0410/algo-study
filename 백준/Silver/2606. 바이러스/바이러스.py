import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
net = []
q = deque(['1'])
virus = 0
for _ in range(m):
    net.append(list(input().split()))

visit = [False] * (n+1)
visit[1] = True

while q:
    target = q.popleft()
    for i in range(m):
        if net[i][0] == target and not visit[int(net[i][1])]:
            visit[int(net[i][1])] = True   
            if net[i][1] not in q :
                q.append(net[i][1])
                virus += 1

        elif net[i][1] == target and not visit[int(net[i][0])]:
            visit[int(net[i][0])] = True   
            if net[i][0] not in q :
                q.append(net[i][0])
                virus += 1

print(virus)