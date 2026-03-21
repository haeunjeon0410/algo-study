import sys
input = sys.stdin.readline

string = {}

for x in range(3):
    s = input().strip()
    string[x] = s

for k, v in string.items():
    if v.isdigit():
        number = int(v)+(3-k)

if number % 3 ==0:
    if number % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")

elif number % 5 == 0:
    print("Buzz")

else:
    print(number)