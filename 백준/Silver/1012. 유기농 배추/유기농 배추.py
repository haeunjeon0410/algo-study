import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def cabbage(x, y):
    movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if not visit[y][x]:
        visit[y][x] = True
        
        for j in range(4):
            di = y + movement[j][0]
            dj = x + movement[j][1]  

            if 0 <= di < n and 0 <= dj < m:
                if (dj, di) in q:
                    cabbage(dj, di)

t = int(input())

for _ in range(t):
    q = []
    worm = 0
    m, n, k = map(int, input().split())

    visit = [[False] * m for _ in range(n)]

    for _ in range(k):
        q.append(tuple(map(int, input().split())))

    for i in range(len(q)):
        x = q[i][0]
        y = q[i][1]

        if not visit[y][x]:
            cabbage(x, y)
            worm += 1

    print(worm)