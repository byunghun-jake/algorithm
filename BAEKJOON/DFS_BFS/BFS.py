# 1. 간선의 정보를 담을 수 있는 2차원 배열을 선언한다.
# 2. 간선의 정보를 저장한다.
# 3. 노드의 방문 여부를 기록할 배열을 선언한다.
# 4. 시작점을 큐에 넣어준다. (시작점을 방문했음을 기록한다.)
# 5. 그래프 탐색을 시작한다.
    # 1. 큐의 0번째 인덱스에 해당하는 값을 기준으로 탐색을 진행한다.
    # 2. 출발 노드를 기준으로 갈 수 있는 노드를 탐색한다. (연결 and 방문기록 x)
    # 3. 갈 수 있는 노드는 큐에 저장한다.
    # 4. 탐색을 완료한 뒤 큐의 0번째 인덱스를 삭제하고 다시 탐색을 진행한다.


N, M, V = map(int, input().split())
NodeMap = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    NodeMap[n1][n2] = NodeMap[n2][n1] = True

queue = [V]
visited = [False] * (N + 1)
visited[V] = True

answer = [V]

while queue:
    start_node = queue[0]
    for next_node in range(1, N + 1):
        if NodeMap[start_node][next_node] and not visited[next_node]:
            queue.append(next_node)
            visited[next_node] = True
            answer.append(next_node)
    else:
        queue.pop(0)

print(answer)
