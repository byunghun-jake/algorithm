# 각 행의 합 / 각 열의 합 / 각 대각선의 합 중 최댓값을 구하는 프로그램

for _ in range(1, 11):
    tc = int(input())

    MAP = []
    for _ in range(100):
        MAP.append(list(map(int, input().split())))

    max_sum = 0

    x1_sum = 0
    x2_sum = 0
    for r in range(100):
        row_sum = 0
        col_sum = 0
        x1_sum += MAP[r][r]
        x2_sum += MAP[r][-r - 1]
        for c in range(100):
            row_sum += MAP[r][c]
            col_sum += MAP[c][r]
        max_sum = max(max_sum, row_sum, col_sum)

    max_sum = max(max_sum, x1_sum, x2_sum)
    print(f"#{tc} {max_sum}")
