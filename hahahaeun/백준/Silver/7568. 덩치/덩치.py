import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    w, h = map(int, input().split())
    people.append((w,h))

for i in range(n):
    count = 0; rank = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    print(rank)



