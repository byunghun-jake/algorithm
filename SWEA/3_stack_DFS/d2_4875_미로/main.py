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


def dfs(start_node, arr_length):
    stack = [start_node]
    visited = [[False] * arr_length for _ in range(arr_length)]
    res = 0

    while stack and res == 0:
        cr, cc = stack.pop()
        visited[cr][cc] = True
        for idx in range(4):
            r = cr + dr[idx]
            c = cc + dc[idx]
            # 인덱스 조건
            if -1 < r < arr_length and -1 < c < arr_length:
                # 도착했다면?
                if maze[r][c] == 3:
                    res = 1
                    break
                elif maze[r][c] == 0 and not visited[r][c]:
                    stack.append((r, c))
    return res


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
    # result = dfs((sr, sc), N)

    ##############################
    visited2 = [[False] * N for _ in range(N)]
    result = dfs2((sr, sc))

    # # 시작지점 stack에 담기
    # stack = [(sr, sc)]
    # # 방문한 좌표 저장할 배열 생성
    # visited = [[False] * N for _ in range(N)]
    # # 도착지점을 찾았는지 확인하는 플래그
    # result = 0
    #
    # # 미로 탐색 시작
    # while stack and result == 0:
    #     # 스택에 담긴 값을 꺼낸다
    #     cr, cc = stack.pop()
    #     # 현재 위치에 방문했음을 저장한다.
    #     visited[cr][cc] = True
    #
    #     # 유망성을 확인한다
    #     for i in range(4):
    #         r = cr + dr[i]
    #         c = cc + dc[i]
    #         if -1 < r < N and -1 < c < N:
    #             if maze[r][c] == 3:
    #                 result = 1
    #                 break
    #             elif maze[r][c] == 0 and not visited[r][c]:
    #                 stack.append((r, c))

    print(f"#{tc} {result}")
