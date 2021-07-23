# DFS(stack)
# BFS(queue)

import sys
from collections import deque

# N: 정점의 개수 (~1,000)
# M: 간선의 개수 (~10,000)
# V: 시작할 점점의 위치

N, M, V = map(int, input().split())

# 0번 인덱스는 사용하지 않는다.
node_map = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    N1, N2 = map(int, sys.stdin.readline().strip().split())
    node_map[N1][N2] = 1
    node_map[N2][N1] = 1

# DFS
# stack에 시작정점을 넣는다.
# visited에 시작 위치 방문을 체크한다.
stack = [V]
dfs_visited = [V]

while stack:
    # stack의 가장 위 값이 출발 정점이 된다.
    s = stack[-1]

    # 출발 정점에서 갈 수 있는 곳을 확인한다.
    for e in range(1, N + 1):
        if node_map[s][e] and e not in dfs_visited:
            dfs_visited.append(e)
            stack.append(e)
            break
    # 갈 수 있는 곳이 없었다면,
    else:
        # 이전 분기로 이동하기 위해, 현재 분기 위치는 삭제한다.
        stack.pop()
        continue


queue = deque([V])
bfs_visited = [V]

while queue:
    # 가장 앞에 있는 값이 출발 정점
    s = queue.popleft()

    # 시작 정점에서 갈 수 있는 정점 찾기
    for e in range(1, N + 1):
        if node_map[s][e] and e not in bfs_visited:
            queue.append(e)
            bfs_visited.append(e)


print(*dfs_visited)
print(*bfs_visited)