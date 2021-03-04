# dfs()로 전달하는 인자를 시작 인덱스와 끝 인덱스로 하는 경우
import sys

sys.stdin = open("input.txt")


def dfs(s, e):
    pass


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    CARDS = list(map(int, input().split()))

    result = dfs(0, N - 1)