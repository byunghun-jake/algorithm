# 가장 기본 모양을 파악한다.
# 3가지의 기본 모양이 있다
    # 10x20 (1개) / 20x20 (2개)

# 종이를 붙이는 방향은 한 방향으로 고정한다. (오른쪽)
import sys

sys.stdin = open("input.txt")


def solve(l):
    if l == 10:
        return 1
    if l == 20:
        return 3
    return solve(l-10) + solve(l-20) * 2


# def solve(x):
#     if x == N:
#         return 1
#     if x > N:
#         return 0
#     return solve(x + 10) + solve(x + 20) * 2


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    result = solve(N)
    print(result)
