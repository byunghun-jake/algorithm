# 모두 같은 색이 아니라면?
    # 4개의 사각형으로 나눈다.
        # 각각의 사각형은 왼쪽위 / 오른쪽위 / 왼쪽아래 / 오른쪽아래로 나누어 진다.

def solve(cr, cc, n):
    # 모두 같은 색인지 확인
    color = BOARD[cr][cc]
    is_same = True
    for r in range(cr, cr + n):
        for c in range(cc, cc + n):
            if color != BOARD[r][c]:
                is_same = False
                break
        if not is_same:
            break
    if is_same:
        # 사각형의 색 카운트
        answer[color] += 1
    else:
        # 4개의 사각형으로 쪼개기
        mid = n // 2
        solve(cr, cc, mid)
        solve(cr, cc + mid, mid)
        solve(cr + mid, cc, mid)
        solve(cr + mid, cc + mid, mid)


N = int(input())

BOARD = [list(map(int, input().split())) for _ in range(N)]

# 하얀색 종이의 수 / 파란색 종이의 수
answer = [0, 0]
solve(0, 0, N)
print(answer[0])
print(answer[1])