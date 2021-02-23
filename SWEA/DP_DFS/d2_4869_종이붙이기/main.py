# stack 문제
# 경우의 수 놀이
# 10x20 / 20x20 직사각형 종이를 잔뜩!
# 높이가 20이고 너비가 N인 직사각형을 만드는 경우의 수는?
import sys

sys.stdin = open("input.txt")


# 재귀 문제이므로, 메모이제이션을 추가해보자
memo = [0] * 31


def dp(n):
    # 너비가 10인 경우 1가지
    if n == 1:
        memo[n] = 1
    # 너비가 20인 경우 3가지
    elif n == 2:
        memo[n] = 3

    if memo[n] == 0:
        memo[n] = dp(n-1) + dp(n-2) * 2

    return memo[n]


# T: 테스트 케이스 수
T = int(input())
for tc in range(1, T+1):
    # W: 만들 직사각형의 너비
    W = int(input()) // 10

    # 너비 10 => 1가지
    # 너비 20 => 3가지

    # 너비 30 => 5가지
    # 너비 20에서 10x20을 1개 붙인 경우 => f(2) 3가지
    # 너비 10에서 너비 20을 붙인 경우 => f(1) * 2

    # 너비 40 => 11개
    # 너비 30에서 10x20을 붙인 경우 => f(3) * f(1)
    # 너비 20에서 20x20을 붙인 경우 => f(2) * f(2)

    result = dp(W)

    print(f"#{tc} {result}")






























