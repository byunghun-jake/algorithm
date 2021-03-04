# 스택을 이용
# 여는 괄호를 만나면 스택에 추가
# 닫는 괄호를 만나면 스택 상단에 있는 값을 꺼내 비교
import sys

sys.stdin = open("input.txt")

TC = int(input())
for tc in range(1, TC+1):
    TEXT = list(input())

    # stack
    stack = []

    # result
    result = 1

    # TEXT 순환
    for letter in TEXT:
        if letter == "(" or letter == "{":
            stack.append(letter)
        elif letter == ")" or letter == "}":
            if not stack:
                result = 0
                break
            else:
                if letter == ")" and stack[-1] == "(":
                    stack.pop()
                elif letter == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    result = 0
                    break
    if stack:
        result = 0
    print(result)