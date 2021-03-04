# NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램
# 도착할 수 있으면, 1
# 도착할 수 없으면, 0

# 미로 설명
# 갈 수 없는 곳: 1
# 갈 수 있는 곳: 0
# 출발 지점: 2
# 도착 지점: 3
import sys

sys.stdin = open("input.txt")


def dfs2(current_node):
    cr = current_node[0]
    cc = current_node[1]
    visited2[cr][cc] = True

    # 종료 조건
    if maze[cr][cc] == 3:
        return 1

    # 유망성 탐색
    for idx in range(4):
        r = cr + dr[idx]
        c = cc + dc[idx]

        if -1 < r < N and -1 < c < N and not visited2[r][c] and maze[r][c] != 1:
            if dfs2((r, c)) == 1:
                return 1
    else:
        return 0



# delta 세팅
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

TC = int(input())
for tc in range(1, TC+1):
    # N: 미로의 크기
    N = int(input())

    maze = []
    for _ in range(N):
        maze.append(list(map(int, list(input()))))

    # 출발지점 찾기
    sr = -1
    sc = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr = i
                sc = j
                break
        if sr != -1:
            break

    visited2 = [[False] * N for _ in range(N)]
    result = dfs2((sr, sc))

    print(f"#{tc} {result}")
