# 문자열을 순회한다.
# 스택 가장 위에 있는 문자와 현재 문자를 비교한다.
# 문자가 다르다면, 현재 문자를 스택에 추가한다.
# 문자가 같다면, 생략
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # TEXT: 입력받을 문자열
    TEXT = list(input())

    # stack: 문자를 담을 스택
    stack = []

    # 문자열 순회
    for word in TEXT:
        # stack에 문자가 담겨있지 않다면
        if not stack:
            stack.append(word)
            continue

        # stack 상단에 있는 문자와 비교
        top = stack.pop()
        if top != word:
            stack.append(top)
            stack.append(word)

    result = len(stack)

    print(f"#{tc} {result}")













































