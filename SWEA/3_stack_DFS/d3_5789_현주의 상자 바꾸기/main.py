# 1 ~ N번까지 N개의 상자
# Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경
# L번 상자부터 R번 상자까지의 값을 i로 변경

import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 상자의 개수
    # Q: 상자 변경 횟수
    N, Q = map(int, input().split())

    # 상자 만들기
    # 1부터 시작하는 박스의 index를 맞추기 위해 +1을 해줍니다.
    boxes = [0] * (N+1)

    # 상자에 적힌 값 바꾸기
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        # L부터 R까지 박스의 값을 i로 변경합니다.
        for idx in range(L, R+1):
            boxes[idx] = i

    # box의 0번째 인덱스를 제거합니다.
    boxes = boxes[1:]
    print(f"#{tc}", *boxes)


























