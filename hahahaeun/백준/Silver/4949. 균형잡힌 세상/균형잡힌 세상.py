import sys
input = sys.stdin.readline

while True:
    stack = []
    case = input()
    s = "".join(case.split())
    string = list(s)
    result = 1

    if case[0] == '.' and len(case) == 2:
        break

    else:
        for i in range(len(string)):
            if string[i] == '(' or string[i] == '[':
                stack.append(string[i])
        

            elif string[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    result = 0
                    break
        
            elif string[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    result = 0
                    break

    if result == 1 and len(stack) == 0:
        print('yes')
    else:
        print('no')
