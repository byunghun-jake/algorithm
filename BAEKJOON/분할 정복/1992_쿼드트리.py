# 왼쪽 위 사각형에서 탐색을 시작할 때, 괄호를 열고
# 오른쪽 아래 사각형에서 탐색이 끝났을 때 괄호를 닫는다.

def solve(cr, cc, n):
    global answer
    # 같은 색인지 확인
    color = BOARD[cr][cc]
    is_same_color = True
    for r in range(cr, cr + n):
        for c in range(cc, cc + n):
            if color != BOARD[r][c]:
                is_same_color = False
                break
        if not is_same_color:
            break
    # 같은 색이라면
    if is_same_color:
        answer.append(color)
    else:
        # 사각형으로 나눈다.
        mid = n // 2
        answer.append("(")
        solve(cr, cc, mid)
        solve(cr, cc + mid, mid)
        solve(cr + mid, cc, mid)
        solve(cr + mid, cc + mid, mid)
        answer.append(")")


N = int(input())
BOARD = [input() for _ in range(N)]
answer = []

solve(0, 0, N)
print("".join(answer))
