import sys

sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    # 8개의 숫자 입력받기
    nums = list(map(int, input().split()))
    # num: 뺄 수
    num = 0

    while nums[-1]:
        num = (num % 5) + 1
        front = nums.pop(0)
        front -= num
        if front < 0:
            front = 0
        nums.append(front)

    print(f"#{tc}", *nums)