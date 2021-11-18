# 스택을 하나 만든다.
# 초기화: 입력받은 문자열 중 0번째 문자를 넣는다.
# 1번째 문자부터 스택에 넣는 작업을 한다.
# 스택에 넣기 전, 스택에 값이 있다면 / 스택의 가장 위에 있는 값과 지금 넣으려고 하는 값이 같은지 확인한다.
# 만약 스택 가장 위에 있는 값과 넣으려는 값이 같다면, 스택 가장 위에 있는 값을 꺼내고 현재 값은 넣지 않는다.
# 만약 다르다면, 현재 값을 스택에 append 한다.

T = int(input())

for _ in range(T):
    text = list(input())
    stack = []

    for w in text:
        if stack:
            if stack[-1] == w:
                stack.pop()
                continue
        stack.append(w)

    print(len(stack))