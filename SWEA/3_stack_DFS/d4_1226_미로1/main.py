# 현재 위치를 기준으로 분기점이 있으면, 스택에 추가
import sys

sys.stdin = open("input.txt")

# d: 탐색 방향
delta_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]


for _ in range(10):
    tc = int(input())
    # 16x16 미로를 2차원 배열에 저장한다.
    maze = []
    for _ in range(16):
        maze.append(list(map(int, list(input()))))

    # print(maze)

    # 시작 지점을 찾는다
    S = None
    find_flag = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                S = (i, j)
                find_flag = True
                break
        if find_flag:
            break

    stack = []
    visited = [[False] * 16 for _ in range(16)]

    stack.append(S)

    can_reach_end = 0

    while stack and can_reach_end == 0:
        current_node = stack.pop()
        visited[current_node[0]][current_node[1]] = True

        # 유망성 탐색
        for delta in delta_list:
            r = current_node[0] + delta[0]
            c = current_node[1] + delta[1]
            if maze[r][c] == 3:
                # 게임 종료
                can_reach_end = 1
                break

            if maze[r][c] == 0 and not visited[r][c]:
                stack.append((r, c))

    print(f"#{tc} {can_reach_end}")
