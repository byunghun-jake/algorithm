import sys

sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc, N = map(int, input().split())

    path = [[-1] * 100 for _ in range(2)]

    input_text = list(map(int, input().split()))

    for i in range(0, N * 2, 2):
        s = input_text[i]
        e = input_text[i+1]

        if path[0][s] == -1:
            path[0][s] = e
        else:
            path[1][s] = e

    # 길 찾기 시작
    stack = []
    visited = [False] * 100

    stack.append(0)

    result = 0

    while stack:
        current_node = stack.pop()
        visited[current_node] = True

        if current_node == 99:
            result = 1
            break

        for i in range(2):
            next_node = path[i][current_node]
            if next_node != -1 and not visited[next_node]:
                stack.append(next_node)

    print(result)