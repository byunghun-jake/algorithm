# N = 100,000
# 시간제한: 2초

N = int(input())
A = list(map(int, input().split()))
M = int(input())
NUMS = list(map(int, input().split()))


# 1. 처음부터 탐색하기 (시간 초과)
# 왜 시간초과가 날까?
    # 가장 오래 걸리는 경우의 수는 N = 100,000 / M = 100,000인 경우로
    # (100,000)^2 번 연산이 이루어지는 경우이다.
    # 10,000,000,000 => 100억 => 1초에 1억번 연산으로 어림잡는다면, 100초가 걸리는 셈 

# for num in NUMS:
#     if num in A:
#         print(1)
#     else:
#         print(0)
        

# 2. 이분 탐색
# 탐색할 A를 정렬한 뒤, 이분 탐색을 진행한다.
    # 1. A를 오름차 순으로 정렬한다.
    # 2. A의 가운데 값과 비교한다.
        # 가운데 값보다 작다면, 그 밑에 있는 값들을 가지고 2번을 진행한다.
        # 가운데 값보다 크다면, 그 위에 있는 값들을 가지고 2번을 진행한다.
        # 가운데 값과 같다면, 탐색 종료

def solve(s_idx, e_idx, n):
    mid_idx = (e_idx + s_idx) // 2
    if s_idx > e_idx:
        print(0)
        return

    if A[mid_idx] == n:
        print(1)
        return
    elif A[mid_idx] > n:
        solve(s_idx, mid_idx - 1, n)
    elif A[mid_idx] < n:
        solve(mid_idx + 1, e_idx, n)

A.sort()
for num in NUMS:
    solve(0, N - 1, num)
