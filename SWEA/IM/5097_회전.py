from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    q = deque(nums)
    for _ in range(M):
        a = q.popleft()
        q.append(a)
    print(q[0])