import sys

sys.stdin = open("input.txt")

# 2. 중심으로 부터의 거리를 이용하는 방식
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    middle = N // 2

    farm = [list(map(int, list(input()))) for _ in range(N)]

    count = 0
    for r in range(N):
        for c in range(N):
            dr = middle - r
            if dr < 0:
                dr = -dr
            dc = middle - c
            if dc < 0:
                dc = -dc

            if 0 <= dr + dc <= middle:
                count += farm[r][c]

    print(f"#{tc} {count}")













































