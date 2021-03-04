# 10개의 테스트 케이스
# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오
# 괄호의 유효성 여부는 항상 옳은 경우만 주어진다
# 연산자는 +와 * 두 종류이다.
# 숫자는 0 ~ 9의 정수만 주어진다.
# "345+6*+7+"
import sys

sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    TEXT = input()

    # 후위 표기식으로 바꾸는 법
    # 1. 숫자는 출력한다.
    # 2. 연산자와 여는 괄호는 스택에 담는다.
    # +: 1 / *: 2 / (: 3
    # ): 0 => 여는 괄호가 나올 때 까지

    stack = []
    postfix_notation = ""

    for letter in TEXT:
        # 연산자인 경우
        if letter == "*":
            while stack:
                # "*"를 만났을 때, 스택을 꺼내야 하는 경우 = 같은 우선순위의 연산자가 있을 때
                if letter == stack[-1]:
                    postfix_notation += stack.pop()
                else:
                    break
            stack.append(letter)
        elif letter == "+":
            while stack:
                top = stack[-1]
                if top == "+" or top == "*":
                    postfix_notation += stack.pop()
                else:
                    break
            stack.append(letter)
        elif letter == "(":
            stack.append(letter)
        elif letter == ")":
            while stack:
                top = stack[-1]
                if top == "(":
                    # 여는 괄호를 삭제한다.
                    stack.pop()
                    break
                postfix_notation += stack.pop()
            # 닫는 괄호는 추가하지 않는다.
        # 숫자인 경우
        else:
            postfix_notation += letter

    # 스택에 남아있는 연산자를 후위 표기식에 추가해준다.
    while stack:
        postfix_notation += stack.pop()

    # print(postfix_notation)

    # 후위표기식을 계산해보자
    # 1. 숫자는 스택에 넣는다.
    # 2. 연산자를 만나면 스택에서 두 값을 꺼내, 연산 후 결과를 스택에 넣는다.
    # 3. 연산이 끝나면, 스택에 남은 값을 출력한다.

    stack = []
    for letter in postfix_notation:
        if letter == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif letter == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        else:
            stack.append(int(letter))

    result = stack.pop()
    print(f"#{tc} {result}")