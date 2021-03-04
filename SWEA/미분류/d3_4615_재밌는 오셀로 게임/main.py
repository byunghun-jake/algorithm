import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 보드 크기
    # M: 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split())

    board = [[0] * (N+4) for _ in range(N+4)]

    # 보드 초기화 (가운데에 돌 놓기)
    start_idx = (N+3) // 2
    for i in range(start_idx, start_idx + 2):
        for j in range(start_idx, start_idx + 2):
            if i == j:
                board[i][j] = 2
            else:
                board[i][j] = 1
    print(board)

    # 돌을 놓는 횟수 만큼 반복
    for _ in range(M):
        x, y, stone = map(int, input().split())
        x += 1
        y += 1
        # 돌 놓기
        board[x][y] = stone

        # 주변 탐색하기
        for i in range(-1, 2):
            for j in range(-1, 2):
                # 다른 색의 돌이 있다면?
                new_x = x + i
                new_y = y + j
                # 같은 색의 돌이 나올 때 까지 사이에 있는 돌의 색을 바꾼다.
                while board[new_x][new_y] != stone and board[new_x][new_y] != 0:
                    board[new_x][new_y] = stone
                    new_x += i
                    new_y += j
    count_black = 0
    count_white = 0
    for i in range(N+4):
        for j in range(N+4):
            if board[i][j] == 1:
                count_black += 1
            elif board[i][j] == 2:
                count_white += 1
    print(count_black, count_white)

































