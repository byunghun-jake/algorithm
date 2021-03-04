# 재귀호출을 이용하여 거듭제곱을 구현하라
import sys

sys.stdin = open("input.txt")


def multi(n, count):
    if count == 1:
        return n
    return n * multi(n, count-1)


for _ in range(10):
    tc = int(input())
    # N: 곱할 값
    # M: 곱할 횟수
    N, M = map(int, input().split())

    result = multi(N, M)

    print(f"#{tc} {result}")








































