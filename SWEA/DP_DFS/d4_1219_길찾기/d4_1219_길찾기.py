# 길을 따라 간다.
# 더이상 진행할 수 없다면, 뒤로 돌아간다.
# 경로는 2x100인 2차원 배열에 저장한다.
import sys

sys.stdin = open("input.txt")


T = 10
for _ in range(1, T+1):
    # tc: 테스트 케이스 번호
    # R: 경로 개수
    tc, R = map(int, input().split())

    # route: 경로
    route = list(map(int, input().split()))

    # 경로 정보를 담을 배열 선언
    adj = [[0] * 100 for _ in range(2)]

    # 경로 정보를 순회하며, 2차원 행렬에 저장
    for i in range(0, R):
        s = route[i*2]
        e = route[i*2 + 1]
        if adj[0][s] == 0:
            adj[0][s] = e
        else:
            adj[1][s] = e

    # 경로 정보가 담긴 배열을 이용해 경로를 탐색한다.
    visited = [False] * 100
    # 시작지점 초기화
    stack = [0]
    # 결과 값 초기화
    result = 0
    
    while stack and result == 0:
        s = stack[-1]
        visited[s] = True

        for i in range(2):
            next_node = adj[i][s]
            if next_node == 99:
                result = 1
                break
            if next_node != 0 and not visited[next_node]:
                stack.append(next_node)
                break
        else:
            stack.pop()

    print(f"#{tc} {result}")
































