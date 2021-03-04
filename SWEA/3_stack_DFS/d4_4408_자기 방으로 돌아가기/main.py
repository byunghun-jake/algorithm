# 가장 많이 겹친 경로의 개수를 찾으면 되겠다
#
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 돌아가야 할 학생의 수
    N = int(input())

    # visited: 각 방별 방문 횟수
    visited = [0] * 401
    # highest visited: 최다 방문 횟수
    highest_visited = 0

    # 학생들의 경로 저장
    for _ in range(N):
        s, e = map(int, input().split())
        if e < s:
            s, e = e, s
        # 1 - 2 // 3 - 4 // 짝을 맞추기 위해 짝수로 통일
        e = int((e - 2 + e % 2) / 2)
        s = int((s - 2 + s % 2) / 2)

        # 어느 방 앞을 지나가는지 저장
        for i in range(s, e+1):
            visited[i] += 1
            if highest_visited < visited[i]:
                highest_visited = visited[i]
    # print(visited)
    print(f"#{tc} {highest_visited}")








































