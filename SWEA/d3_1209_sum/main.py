import sys

sys.stdin = open("input.txt")

for test_case in range(10):
    tc = int(input())
    biggest_sum = 0

    # 100 x 100 행렬 입력받기
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # print(arr)

    # 열을 순환하며, 합을 구해보기
    for r in range(len(arr)):
        r_sum = 0
        for c in range(len(arr[r])):
            r_sum += arr[r][c]
        if biggest_sum < r_sum:
            biggest_sum = r_sum

    # 행을 순환하며, 합을 구해보기
    for c in range(100):
        c_sum = 0
        for r in range(100):
            c_sum += arr[r][c]
        if biggest_sum < c_sum:
            biggest_sum = c_sum

    # 대각선 순환하며, 합을 구해보기
    h_sum1 = 0
    h_sum2 = 0
    for r in range(100):
        h_sum1 += arr[r][r]
        h_sum2 += arr[r][99-r]
    if biggest_sum < h_sum1:
        biggest_sum = h_sum1
    if biggest_sum < h_sum2:
        biggest_sum = h_sum2

    print(f"#{tc} {biggest_sum}")














