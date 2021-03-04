import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * (N + 2) for _ in range(N + 2)]

    # 첫 돌을 배치
    mid = N // 2
    board[mid][mid] = 2
    board[mid][mid + 1] = 1
    board[mid + 1][mid] = 1
    board[mid + 1][mid + 1] = 2

    # delta
    delta_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # 돌을 놓자
    for _ in range(M):
        R, C, color = map(int, input().split())

        # 해당 위치에 돌을 놓기
        board[R][C] = color

        for d in delta_list:
            stack = []
            r = R + d[0]
            c = C + d[1]

            while board[r][c] != 0:
                if board[r][c] == color:
                    while stack:
                        top = stack.pop()
                        board[top[0]][top[1]] = color
                    break
                else:
                    stack.append((r, c))
                r += d[0]
                c += d[1]

    b_count = 0
    w_count = 0
    for r in range(N + 2):
        for c in range(N + 2):
            if board[r][c] == 1:
                b_count += 1
            elif board[r][c] == 2:
                w_count += 1

    print(f"#{tc} {b_count} {w_count}")


























