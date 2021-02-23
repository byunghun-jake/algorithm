# 1. 여는 괄호를 만나면, 스택에 추가한다.
# 2. 닫는 괄호를 만나면, 스택 상단에 있는 값을 꺼내 같은 타입인지 비교한다.
    # 2-1. 타입이 같다면, 스택 상단 값을 제거한다.
    # 2-2. 타입이 다르다면, 탐색을 중단한다.
import sys

sys.stdin = open("input.txt")

O_bracket = ["(", "{"]
C_bracket = [")", "}"]


# T: 테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    # TEXT = 탐색할 문자열
    TEXT = list(input())
    # print(TEXT)
    
    # stack: 여는 괄호를 담을 스택
    stack = []
    # result: 판단 결과
    result = 1

    # 문자열 TEXT를 탐색한다.
    for word in TEXT:
        # 여는 괄호를 만나면 스택에 추가한다.
        if word in O_bracket:
            stack.append(word)
        
        # 닫는 괄호를 만나면, 스택 상단에 있는 값을 꺼내 타입이 같은지 비교한다.
        if word in C_bracket:
            # 스택에 아무것도 담겨있지 않은데 닫는 괄호를 만났다면, 탐색을 중단한다.
            if len(stack) == 0:
                result = 0
                break
            
            top = stack[-1]
            O_index = O_bracket.index(top)
            C_index = C_bracket.index(word)
            
            if O_index != C_index:
                # 닫는 괄호와 여는 괄호의 타입이 다르다면, 탐색을 중단한다.
                result = 0
                break
            else:
                # 타입이 같다면, 꺼냈던 괄호를 스택에서 삭제한다.
                stack.pop()
                
    # 탐색이 중단되지 않고 끝까지 진행
    else:
        if len(stack) != 0:
            # stack에 아직 괄호가 남아있다면, 짝이 맞지 않은 것
            result = 0

    print(f"#{tc} {result}")





























