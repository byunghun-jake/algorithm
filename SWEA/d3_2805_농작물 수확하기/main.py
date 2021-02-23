import sys

sys.stdin = open("input.txt")

# T: 테스트 케이스의 개수
T = int(input())
for tc in range(1, T+1):
    # N: 농장 크기
    N = int(input())
    mid = N // 2

    farm = [list(map(int, str(input()))) for _ in range(N)]

    # 농장을 순회
    total = 0
    sub_farm = []
    for r in range(N):
        if r <= mid:
            for c in range(mid-r, mid+r+1):
                total += farm[r][c]
                sub_farm.append(farm[r][c])
        else:
            for c in range(r-mid, N-(r-mid)):
                total += farm[r][c]
                sub_farm.append(farm[r][c])
    print(f"#{tc} {total}")


































