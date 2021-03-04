# N-Queen 문제와 유사하다
# 순열을 구하자
import sys

sys.stdin = open("input.txt")


def dfs(idx, visited, total):
    global min_total
    # idx: 행을 의미하는 인덱스
    # visited: 사용된 열을 저장한 배열
    # total: 현재 행까지의 누적합
    if idx == N:
        if min_total > total:
            min_total = total
            print(total)
        return
    # 아직 모든 누적합을 구하지는 않았지만, 최소합보다 크거나 같은 경우에는 더이상 계산하지 않는다.
    if min_total <= total:
        return

    # 현재 행에서 선택할 수 있는 열을 확인
    for i in range(N):
        if not visited[i]:
            # 현재 행에서 i열을 사용하였음을 표시
            visited[i] = True
            dfs(idx + 1, visited, total + DATA[idx][i])
            # 현재 행에서 i열을 사용한 경우는 종료되었으니, 원래 상태로 변경
            visited[i] = False


def dfs2():
    visited2 = [False] * N
    stack = []

    for i in range(N):
        # 0번 행의 열을 결정한 후 스택에 추가
        # 
        stack.append((0, i))
        visited2[i] = True
        while stack:
            top = stack.pop()



TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    DATA = [list(map(int, input().split())) for _ in range(N)]
    
    # 순열 만들기
    # visited: 순열을 만드는 데 사용된 열 저장
    visited = [False] * N
    min_total = 10 * N
    dfs(0, visited[:], 0)