T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    NUMS = list(map(int, input().split()))
    print(f"#{tc} {max(NUMS) - min(NUMS)}")