import sys

sys.stdin = open("input.txt")

operator_list = ["+", "*", "/", "-"]


def solve(data):
    stack = []
    for letter in data:
        if letter in operator_list:
            if len(stack) < 2:
                return "error"
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if letter == "+":
                stack.append(num1 + num2)
            elif letter == "*":
                stack.append(num1 * num2)
            elif letter == "/":
                stack.append(num1 // num2)
            else:
                stack.append(num1 - num2)
        elif letter == ".":
            if len(stack) > 1:
                return "error"
            return stack.pop()
        else:
            stack.append(letter)


TC = int(input())
for tc in range(1, TC + 1):
    DATA = input().split()
    result = solve(DATA)
    print(f"#{tc} {result}")