import sys
input = sys.stdin.readline

n = int(input())
list1 = []
for _ in range(n):
    people = list(input().split())
    list1.append(people)

sorted_people = sorted(list1, key=lambda x: int(x[0]))

for x in sorted_people:
    print(" ".join(x))