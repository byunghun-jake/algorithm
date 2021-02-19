import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 문자열 입력 받기(5줄)
    arr = [list(input()) for _ in range(5)]

    # 결과 텍스트
    result = ""

    # 1. 열을 기준으로 순환한다
    # 각 줄의 길이는 1이상 15이하이다
    for c in range(15):
        # 행별로 순환한다
        for r in range(5):
            # 각 줄의 길이는 제각각 다를 수 있으므로, 이를 판단하기 위한 조건이 필요하다
            # 현재 읽고 있는 열보다 길이가 짧은 경우,
            if len(arr[r]) <= c:
                # 건너뛰어야 한다
                continue
            result += arr[r][c]

    print(f"#{tc} {result}")












































