import sys
input = sys.stdin.readline

test = int(input())
sum = 0
for _ in range(test):
    k = int(input())
    n = int(input())
    
    list1 = [[0] * n for _ in range(k+1)]
    
    for j in range(1, k+1):
        sum1 = 0
        for i in range(n):
            list1[0][i] = i+1
            sum1 += list1[j-1][i]
            list1[j][i] = sum1
    print(sum1)