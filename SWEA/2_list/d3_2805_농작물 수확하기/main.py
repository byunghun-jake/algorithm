# N x N 크기의 농장
import sys

sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 결과
    result = 0

    # 행 단위로 순환
    # 양 끝 지점 (L - R)
    L = R = N //2
    # 범위 변경 변수
    dc = 1
    for r in range(N):
        row = list(map(int, list(input())))
        for c in range(L, R+1):
            result += row[c]
        if 0 == L:
            dc = -1
        L -= dc
        R += dc

    print(f"#{tc} {result}")









































