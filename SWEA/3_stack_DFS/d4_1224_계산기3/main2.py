import sys

sys.stdin = open("input.txt")


# 연산자 참조 배열
in_come_priority = {"+": 1, "*": 2, "(": 3, ")": 0}
in_stack_priority = {"+": 1, "*": 2, "(": 0}

def make_postfix(cal):
    # 1. 중위 표기식에서 토큰을 읽는다.
    # 2. 토큰이 피연산자(숫자)이면, 토큰을 출력한다.
    # 3. 토큰이 연산자(괄호포함)일 때, 스택의 top과 우선순위를 비교한다.
        # 1. 토큰의 in_come_priority가 top의 in_stack_priority보다 높은 경우, 스택에 추가한다.
        # 2. top의 우선순위가 더 높거나 같은 경우, 스택에서 꺼내 출력한다.
        # 토큰이 닫는 괄호라면, 여는 괄호가 나올 때까지 스택에서 연산자를 꺼내 출력한 후,
        # 여는 괄호를 스택에서 꺼낸다.

    # result: 출력한 값을 담을 배열
    # stack: 연산자를 담을 배열
    result = []
    stack = []

    for token in cal:
        if token in in_come_priority:
            if not stack:
                stack.append(token)
                continue
            while stack:
                token_priority = in_come_priority.get(token)
                top_priority = in_stack_priority.get(stack[-1])
                if token_priority > top_priority:
                    stack.append(token)
                    break
                else:
                    top = stack.pop()
                    if top == "(":
                        break
                    result.append(top)
        else:
            result.append(token)
    # 스택에 남은 연산자를 출력한다.
    while stack:
        result.append(stack.pop())

    return "".join(result)


def calculator(cal):
    # 숫자를 만나면, 스택에 추가한다.
    # 연산자를 만나면 스택에 있는 숫자 2개를 꺼내, 연산을 수행한 후 결과를 스택에 추가한다.
    stack = []
    for token in cal:
        if token in in_come_priority:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if token == "+":
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)
        else:
            stack.append(token)
    return stack[0]



for tc in range(1, 11):
    N = int(input())
    CAL = input()

    postfix_string = make_postfix(CAL)

    result = calculator(postfix_string)
    print(result)