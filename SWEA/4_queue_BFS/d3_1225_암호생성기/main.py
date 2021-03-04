import sys

sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    # 8개의 숫자 입력받기
    nums = list(map(int, input().split()))
    # num: 뺄 수
    num = 0
    idx = -1

    while True:
        # 대상 숫자 인덱스 세팅
        idx = (idx + 1) % 8

        # 뺄 수를 세팅
        num += 1
        if num > 5:
            num = 1

        nums[idx] -= num
        if nums[idx] <= 0:
            nums[idx] = 0
            break

    result = []
    while len(result) < len(nums):
        idx = (idx + 1) % 8
        result.append(nums[idx])

    print(f"#{tc}", *result)