# 1. 길이가 더 짧은 숫자열을 a에 담고, 긴 숫자열을 b에 담는다.
# 1-1. 두 수열의 길이를 비교하여, a가 더 긴 경우 둘을 바꾸어준다.
# 2. a 숫자열의 인덱스를 옮겨가며, b 숫자열의 동일한 인덱스와 곱한 값을 담는다.
# 3. 곱한 값을 담은 리스트를 순환하며 가장 큰 값을 찾는다.
# 4. 반환한다.
# TODO: 더 간단한 방법 생각해보기 (윈도우 슬라이딩)

import sys

sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    a_length, b_length = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    # 1
    if a_length > b_length:
        a_length, b_length = b_length, a_length
        a_list, b_list = b_list[:], a_list[:]

    multiply_list = [0] * (b_length - a_length + 1)

    # 길이가 긴 리스트를 기준으로 반복
    for i in range(0, b_length - a_length + 1):
        total = 0
        for j in range(a_length):
            total += a_list[j] * b_list[j + i]
        multiply_list[i] = total

    # 최대값 찾기
    max_num = multiply_list[0]
    for num in multiply_list:
        if num > max_num:
            max_num = num

    print(f"#{test_case} {max_num}")

