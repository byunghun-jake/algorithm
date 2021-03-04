# 첫 돌 배치
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

    # 돌을 놓자
    for _ in range(M):
        R, C, stone = map(int, input().split())

        # 해당 위치에 돌을 놓기
        board[R][C] = stone

        # 돌을 놓은 위치를 기준으로 주변을 탐색하여, 상대방 돌을 찾고
        # 상대방 돌이 위치한 방향을 저장한다.
        direction_list = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                r = R + i
                c = C + j
                if board[r][c] != 0 and board[r][c] != stone:
                    direction_list.append((i, j))

        # 찾은 방향으로 진행하기
        # 내 돌이 나오거나, 돌이 없거나, 경계를 넘어가는 경우 중단
        for direction in direction_list:
            stack = []
            r = R + direction[0]
            c = C + direction[1]
            # 탐색 범위를 벗어나는 조건 (테두리 경계가 있기 때문에)
            # 1. 인덱스를 이용한 방법
            # while -1 < r < N + 2 and -1 < c < N + 2:
            # 2. 임의로 추가한 테두리를 이용한 방법
            while board[r][c] != 0:
                if board[r][c] == stone:
                    # 내 돌과 동일한 색이라면,
                    # 지금까지 스택에 쌓아두었던(경로에 있던) 돌을 꺼내 색을 변경한다.
                    # 이 방향으로의 탐색을 종료한다.
                    while len(stack) != 0:
                        top = stack.pop()
                        board[top[0]][top[1]] = stone
                    break
                else:
                    # 기준 돌과 현재 돌이 다른 색이라면, 스택에 현재 좌표를 추가합니다.
                    stack.append((r, c))
                # 작업이 끝나면, 해당 단계로 한번 더 진행한다.
                r += direction[0]
                c += direction[1]
        # for row in board:
        #     print(row)
        # print()

    # 게임이 끝났다면, 판을 순환하여 돌의 개수를 센다.
    b_count = 0
    w_count = 0
    for r in range(N+2):
        for c in range(N+2):
            if board[r][c] == 1:
                b_count += 1
            elif board[r][c] == 2:
                w_count += 1

    print(f"#{tc} {b_count} {w_count}")


















































