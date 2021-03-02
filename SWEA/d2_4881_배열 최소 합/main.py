# NxN 배열에 숫자가 있다.
# 한 줄에 하나씩 N개의 숫자를 골라 합이 최소가 되도록 한다
# 가로, 세로 방향으로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

# 1. 행 우선 순회하여,
import sys

sys.stdin = open("input.txt")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # min_total: 최소 합
    min_total = 10 * N
    # nums: 숫자를 담을 배열
    nums = []
    stack = [(0, i) for i in range(N)]
    visited = []
    r = 0
    while stack:
        cr, cc = stack.pop()
        visited.append(cc)
        nums.append(arr[cr][cc])

        # 이미 숫자의 합이 최소 합보다 크다면, 이 방향으로 더 진행할 필요가 없다.
        if min_total < sum(nums):
            # 복귀
            if stack:
                return_row = stack[-1][0]
                nums = nums[:return_row]
                visited = visited[:return_row]
                continue
        
        r = cr + 1
        if r == N:
            # 지금까지 쌓인 숫자를 합해 계산
            total = sum(nums)
            if min_total > total:
                min_total = total

            # 복귀
            if stack:
                # 복귀 지점 파악
                return_row = stack[-1][0]
                nums = nums[:return_row]
                visited = visited[:return_row]
                continue

        for c in range(N):
            if c not in visited:
                stack.append((r, c))

    print(f"#{tc} {min_total}")