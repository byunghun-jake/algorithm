# 쇠 막대기의 시작과 끝을 정하고, 다음 레이저가 위치한 곳 까지

import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    pipe = list(input())
    L = len(pipe)
    
    # 막대기를 순환하며, 괄호가 열리고 닫힐 때 작업을 수행하자
    # 1. 괄호가 열릴 때, 현재 열린 괄호의 개수에 1을 추가한다.
    # 2. 괄호가 닫힐 때,
    # 2-1. 열린 괄호의 개수를 1 줄인다.
    # 2-2. 이전 괄호가 열림 괄호라면, 레이저라는 뜻.
    # 2-2-1. 지금까지 열린 괄호의 개수만큼 파이프가 잘려나갔으니, 잘린 파이프 개수에 추가해준다.
    # 2-3. 이전 괄호가 열림 괄호가 아니라면,
    # 2-3-1. 파이프 1개가 끝났으니, 잘린 파이프 개수에 1을 추가한다.

    cut_pipe = 0
    current_pipe = 0
    for idx in range(L):
        if pipe[idx] == "(":
            current_pipe += 1
        else:
            current_pipe -= 1
            is_lazar = pipe[idx-1] == "("
            if is_lazar:
                cut_pipe += current_pipe
            else:
                cut_pipe += 1

    print(f"#{tc} {cut_pipe}")







































