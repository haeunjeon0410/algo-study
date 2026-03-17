import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

target = v - a
days = target // (a-b)

if target % (a-b) == 0:
    print(days+1)
else:
    print(days+2)