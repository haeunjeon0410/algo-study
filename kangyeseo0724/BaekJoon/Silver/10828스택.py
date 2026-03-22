import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    inst = sys.stdin.readline().split()
    
    if inst[0] == "push":
        stack.append(inst[1])
    
    elif inst[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
            
    elif inst[0] == "size":
        print(len(stack))
        
    elif inst[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    
    elif inst[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        
    