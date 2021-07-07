# 4개의 분할된 면을 순환하는 순서
# 2사분면 > 1사분면 > 3사분면 > 4사분면

def check_all_color_same(r, c, n):
    color = DISPLAY[r][c]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != DISPLAY[i][j]:
                return False
    return True


def solve(r, c, n):
    global answer

    # 같은 색으로 이루어졌는지 탐색
    if check_all_color_same(r, c, n):
        answer += f"{DISPLAY[r][c]}"
        return
    else:
        answer += "("

        # 4분할
        mid = n // 2
        solve(r, c, mid)
        solve(r + mid, c, mid)
        solve(r, c + mid, mid)
        solve(r + mid, c + mid, mid)

    answer += ")"


N = int(input())
DISPLAY = [input() for _ in range(N)]
answer = ""

solve(0, 0, N)

print(answer)