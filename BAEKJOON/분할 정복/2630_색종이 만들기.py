# 색종이 탐색
# 다른 색이 나오면, 4개로 분할
# 4개로 분할한 각각의 색종이를 탐색
# 다른 색이 나오면, 4개로 분할
# 4개로 분할한 각각의 색종이를 탐색
# 모두 같은 색이 나오면, 갯수 +1

def check_board_color(r, c, n):
    color = BOARD[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != BOARD[i][j]:
                return False
    return True


def solve(r, c, n):
    # board 탐색
    if check_board_color(r, c, n):
        # 해당하는 색 카운팅
        color = BOARD[r][c]
        paper_count[color] += 1
    else:
        # 4개로 분할한 뒤 재귀호출
        mid = n // 2
        # 2사분면
        solve(r, c, mid)
        # 1사분면
        solve(r + mid, c, mid)
        # 3사분면
        solve(r, c + mid, mid)
        # 4사분면
        solve(r + mid, c + mid, mid)


N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]
paper_count = [0, 0]

solve(0, 0, N)
print(paper_count[0])
print(paper_count[1])
