# N: 수빈이 위치(~100,000)
# K: 동생 위치 (~100,000)

# 분기점
    # 1. 현재 위치 + 1
    # 2. 현재 위치 - 1
    # 3. 현재 위치 * 2
    # 3가지 경우의 수를 queue에 담는다.

from collections import deque

N, M = map(int, input().split())

# 효율성을 위해 방문 기록을 저장하자
visited = [False] * 100001

dq = deque([[N, 0]])
visited[N] = True
answer = 0

while dq:
    cp, t = dq.popleft()

    if cp < 0:
        continue

    if cp == M:
        answer = t
        break


    # 1. 현재 위치 + 1
    if (cp + 1 in range(100001)) and not visited[cp + 1]:
        dq.append([cp + 1, t + 1])
        visited[cp + 1] = True
    # 2. 현재 위치 - 1
    if (cp - 1 in range(100001)) and not visited[cp - 1]:
        dq.append([cp - 1, t + 1])
        visited[cp - 1] = True
    # 3. 현재 위치 * 2
    if (cp * 2 in range(100001)) and not visited[cp * 2]:
        dq.append([cp * 2, t + 1])
        visited[cp * 2] = True

print(answer)