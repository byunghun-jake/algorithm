import sys

sys.stdin = open("1210_Ladder1.txt")
# 어느 사다리를 고르면 X표시에 도착하게 될까?

# X 표시에서 거꾸로 올라가는 것으로 전환해보자
# 가로선을 만났을 떄 어떻게 동작해야 할까?
    # 위로 올라가던 중 좌 or 우에 있는 가로선을 만나면, 그 가로선으로 이동한다.
    # 현재 위치에서 좌, 우를 탐색한 뒤
        # 있으면 해당 가로선으로 이동
        # 없으면 위 칸으로 이동
    
    # 좌 or 우로 이동하던 중 위로 갈 수 있는 길을 만나면, 위로 올라간다.

N = 100

for _ in range(1, 11):
    tc = int(input())
    ladder_map = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        ladder_map.append(row)

    # X 위치를 찾는다.
    start_col = 0
    for idx in range(N):
        if ladder_map[N - 1][idx] == 2:
            start_col = idx
            break

    # X 위치를 시작지점으로 탐색을 시작한다.
    cr = N - 1
    cc = start_col
    c_direction = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while cr != 0:
        # 좌
        if cc > 1 and ladder_map[cr][cc - 1] == 1:
            while cc > 0 and ladder_map[cr][cc - 1] == 1:
                cc -= 1
            else:
                cr -= 1
                continue
        # 우
        if cc < 99 and ladder_map[cr][cc + 1] == 1:
            while cc < 99 and ladder_map[cr][cc + 1] == 1:
                cc += 1
            else:
                cr -= 1
                continue
        # 양쪽 다 없을 때
        cr -= 1
        cc = cc
    print(f"#{tc} {cc}")

    