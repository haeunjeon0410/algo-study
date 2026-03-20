import sys
input = sys.stdin.readline

n, m = map(int, input().split())

chess = [list(input().strip()) for _ in range(n)]

min_repair = 64
for a in range(n-7):
    for b in range(m-7):
        
        w_count = 0
        b_count = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: 
                    if chess[i][j] != 'W':
                        w_count += 1
                    else:
                        b_count += 1

                else:
                    if chess[i][j] != 'B':
                        w_count += 1
                    else:
                        b_count += 1
        
        current_min = min(w_count, b_count)
        if current_min < min_repair:
            min_repair = current_min

print(min_repair)
