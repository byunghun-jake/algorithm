# 지게차 이동

# 위, 아래, 오른쪽, 왼쪽으로 이동이 가능하다
    # 위 / 왼쪽은 최단거리로 갈 수 없으므로 제외한다.

# 0, 0에서 출발한다.

dy = [1, 0]
dx = [0, 1]

def solve(count, y, x):
    global min_count
    if count > min_count:
        return

    if y == H - 1 and x == W - 1:
        if count < min_count:
            min_count = count
        return

    if y >= H or x >= W:
        return

    # 아래 마모도와 오른쪽 마모도 확인
    b_count = 99999
    r_count = 99999
    if y + 1 < H:
        b_count = MAP[y + 1][x]
    if x + 1 < W:
        try:
            r_count = MAP[y][x + 1]
        except:
            print(y, x)

    if b_count == r_count:
        used[y + 1][x] = 1
        solve(count + b_count, y + 1, x)
        used[y + 1][x] = 0
    else:
        if y + 1 < H:
            used[y + 1][x] = 1
            solve(count + b_count, y + 1, x)
            used[y + 1][x] = 0
        elif x + 1 < W:
            used[y][x + 1] = 1
            solve(count + r_count, y, x + 1)
            used[y][x + 1] = 0

# H, W = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(H)]


H, W = 4, 4
MAP = [
    [0, 3, 5, 1],
    [1, 1, 1, 5],
    [1, 50, 20, 10],
    [1, 50, 5, 0],
]
used = [[0] * W for _ in range(H)]

min_count = 99999999999999999
solve(0, 0, 0)
print(min_count)