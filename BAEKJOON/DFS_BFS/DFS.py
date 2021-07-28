# 1. 노드 간 연결된 간선을 2차원 배열로 저장한다.
# 2. 방문한 노드인지 아닌지를 알기 위해 배열을 선언한다.
# 3. 시작 노드를 스택에 추가한다.
# 4. 탐색을 시작한다.
    # 1. 스택에 가장 마지막에 들어간 노드를 기준으로 탐색한다.
    # 2. 노드에 방문했음을 기록한다.
    # 3. 갈 수 있는 노드 중 방문하지 않은 노드를 탐색한다.
    # 4. 갈 수 있는 노드가 있다면, 스택에 추가하고 1로 돌아간다.
    # 5. 갈 수 있는 노드가 없다면, pop을 통해 스택의 마지막 값을 제거한다. (뒤로 가기)

N, M, V = map(int, input().split())
NodeMap = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    NodeMap[n1][n2] = NodeMap[n2][n1] = 1

visited = [False] * (N + 1)

stack = [V]

answer = [V]

while stack:
    s = stack[-1]
    visited[s] = True

    for next_node in range(1, N + 1):
        if NodeMap[s][next_node] and not visited[next_node]:
            stack.append(next_node)
            answer.append(next_node)
            break
    else:
        stack.pop()

print(answer)