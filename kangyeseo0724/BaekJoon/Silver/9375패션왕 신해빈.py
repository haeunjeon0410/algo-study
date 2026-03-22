import sys

case = int(sys.stdin.readline())

for _ in range (case):
    n = int(sys.stdin.readline())
    
    clothes = {}
    
    for i in range(n):
        name, category = sys.stdin.readline().split()
        
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
            
    ans = 1
    for val in clothes.values():
        ans *= (val + 1)
    
    print(ans - 1)