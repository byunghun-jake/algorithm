# 앞부터 뒤까지 순서대로 더해가며, 가장 큰 값과 가장 작은 값을 찾아 저장한다.

T = int(input())

for tc in range(1, T + 1):
    min_sum = 987654321
    max_sum = 0
    N, M = map(int, input().split())
    NUMS = list(map(int, input().split()))
    for i in range(0, N - M + 1):
        c_sum = sum(NUMS[i:i+M])
        if min_sum > c_sum:
            min_sum = c_sum
        if max_sum < c_sum:
            max_sum = c_sum
    print(f"#{tc} {max_sum - min_sum}")