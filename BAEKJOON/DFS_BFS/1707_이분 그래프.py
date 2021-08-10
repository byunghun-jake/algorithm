# 인접한 정점들과는 다른 그룹에 속하는지 확인
import sys
from collections import deque


def bfs(sn):
    dq = deque([sn])
    visited[sn] = 1

    while dq:
        cn = dq.popleft()
        for nn in board[cn]:
            # 그룹 확인
            if visited[nn] == 0:
                dq.append(nn)
                visited[nn] = -visited[cn]
            elif visited[nn] == visited[cn]:
                return "NO"
    return "YES"



TC = int(input())
for tc in range(TC):
    node_count, line_count = map(int, input().split())
    board = [[] for _ in range(node_count + 1)]
    visited = [0] * (node_count + 1)

    for _ in range(line_count):
        r, c = map(int, sys.stdin.readline().strip().split())
        board[r].append(c)
        board[c].append(r)

    answer = ""
    for sn in range(1, node_count + 1):
        if not visited[sn]:
            answer = bfs(sn)
            if answer == "NO":
                break
    print(answer)
