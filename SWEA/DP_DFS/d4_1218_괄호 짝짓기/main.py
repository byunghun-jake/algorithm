# 괄호 문자들로 이루어진 문자열을 입력받는다.

import sys

sys.stdin = open("input.txt")

O_bracket = ["(", "{", "[", "<"]
C_bracket = [")", "}", "]", ">"]

for tc in range(1, 11):
    N = int(input())
    BRACKET = list(input())

    stack = []
    result = 1

    for b in BRACKET:
        # 열린 괄호라면?
        if b in O_bracket:
            stack.append(b)
        elif len(stack) == 0:
            result = 0
            break
        else:
            # 닫힌 괄호
            o = stack[-1]
            o_type = O_bracket.index(o)
            c_type = C_bracket.index(b)
            if o_type != c_type:
                result = 0
                break
            else:
                stack.pop()
    print(f"#{tc} {result}")




































