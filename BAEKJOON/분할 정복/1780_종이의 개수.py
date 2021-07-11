# 3등분하는 차이

def solve(cr, cc, n):
    # 탐색
    color = BOARD[cr][cc]
    is_same_color = True
    for r in range(cr, cr + n):
        for c in range(cc, cc + n):
            if color != BOARD[r][c]:
                is_same_color = False
                break
        if not is_same_color:
            break
    # 모든 색이 같을 때,
    if is_same_color:
        answer[color + 1] += 1
    # 모든 색이 같진 않을 때,
    else:
        idx = n // 3
        solve(cr, cc, idx)
        solve(cr, cc + idx, idx)
        solve(cr, cc + (idx * 2), idx)
        solve(cr + idx, cc, idx)
        solve(cr + idx, cc + idx, idx)
        solve(cr + idx, cc + (idx * 2), idx)
        solve(cr + (idx * 2), cc, idx)
        solve(cr + (idx * 2), cc + idx, idx)
        solve(cr + (idx * 2), cc + (idx * 2), idx)


N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]  # -1의 개수 / 0의 개수 / 1의 개수

solve(0, 0, N)
print(answer[0])
print(answer[1])
print(answer[2])
