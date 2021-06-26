# 확인해야 할 것
    # 1. 같은 가로줄
    # 2. 같은 세로줄
    # 3. 3x3 작은 사각형

# 빈칸의 위치를 찾기
# 빈칸의 좌표를 통해 조건 확인
# 조건에 맞지 않는다면 다른 값을 넣기

import sys

BOARD = []
check_small = {
    "00": [0] * 10,
    "01": [0] * 10,
    "02": [0] * 10,
    "10": [0] * 10,
    "11": [0] * 10,
    "12": [0] * 10,
    "20": [0] * 10,
    "21": [0] * 10,
    "22": [0] * 10,
}

for _ in range(9):
    nums = list(map(int, input().split()))
    BOARD.append(nums)

# 빈칸 찾기
check_r = [[0] * 10 for _ in range(9)]
check_c = [[0] * 10 for _ in range(9)]
empty_coord = []
for r in range(9):
    for c in range(9):
        if BOARD[r][c] == 0:
            empty_coord.append((r, c))
            continue
        check_r[r][BOARD[r][c]] = 1
        check_c[c][BOARD[r][c]] = 1
        dict_key = f"{r // 3}{c // 3}"
        check_small[dict_key][BOARD[r][c]] = 1



def solve(idx):
    if idx == len(empty_coord):
        # 출력하기
        for i in range(9):
            print(*BOARD[i])
        return True

    r, c = empty_coord[idx]
    for num in range(1, 10):
        if check_r[r][num] or check_c[c][num] or check_small[f"{r//3}{c//3}"][num]:
            continue
        # 숫자 입력
        check_r[r][num] = 1
        check_c[c][num] = 1
        check_small[f"{r//3}{c//3}"][num] = 1
        BOARD[r][c] = num
        # 다음 빈칸을 채우러
        if solve(idx + 1):
            return True
        # 원상 복귀
        check_r[r][num] = 0
        check_c[c][num] = 0
        check_small[f"{r//3}{c//3}"][num] = 0

solve(0)