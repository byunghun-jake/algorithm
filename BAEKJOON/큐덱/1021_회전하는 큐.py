# N: 큐의 크기 [1 ~ N]
# M: 뽑을 수의 개수 (탐색 횟수)
N, M = map(int, input().split())

NUMS = list(map(int, input().split()))
deque = [i for i in range(1, N + 1)]
step = 0

# 수를 뽑는 만큼 작업을 시작합니다.
for i in range(M):
    # 뽑을 수를 찾습니다.
    num = NUMS[i]
    # 뽑을 수가 몇 번째 인덱스에 있는지 확인
    idx = deque.index(num)
    l_step = idx - 0
    r_step = len(deque) - idx
    step += min(l_step, r_step)
    deque = deque[idx + 1:] + deque[:idx]


print(step)


