import sys
input = sys.stdin.readline

while True:
    result = 1
    case = input().strip()
    if case == '0':
        break
    
    for i in range(len(case)):
        if i <= len(case) // 2 and case[i] != case[-i-1]:
            result = 0
            break
        else:
            continue

    if result:
        print('yes')

    else:
        print('no')