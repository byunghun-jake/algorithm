# 숫자는 스택에 넣는다
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# .은 스택에서 숫자를 꺼내 출력한다.
import sys

sys.stdin = open("input.txt")

TC = int(input())
for tc in range(1, TC+1):
    TEXT = list(input().split())
    result = 0
    stack = []
    calculation_flag = True

    # TEXT를 순환하며, 작업을 수행한다.
    for letter in TEXT:
        if not calculation_flag:
            result = "error"
        elif letter == ".":
            if len(stack) == 1:
                result = stack.pop()
                calculation_flag = False
            else:
                result = "error"
        elif letter == "+" or letter == "/" or letter == "*" or letter == "-":
            if len(stack) < 2:
                result = "error"
                break
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if letter == "+":
                    res = num1 + num2
                elif letter == "-":
                    res = num1 - num2
                elif letter == "*":
                    res = num1 * num2
                else:
                    res = int(num1 / num2)
                stack.append(res)
        else:
            num = int(letter)
            stack.append(num)

    print(f"#{tc} {result}")