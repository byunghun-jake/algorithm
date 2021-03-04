# 1. num_list 를 정렬한다.
# 2. 모든 구간을 순회하며 num_range 만큼 잘라 부분수열을 만든다.
# 3. 두 부분수열 각각의 합을 구하고 그 차를 출력한다.

import sys

sys.stdin = open("./input.txt")


T = int(input())
for test_case in range(1, T + 1):
    num_count, num_range = map(int, input().split())
    num_list = list(map(int, input().split()))
    min_sum = 50 * 10000
    max_sum = 0
    for i in range(num_count - num_range + 1):
        sub_nums = num_list[i:i+num_range]
        sub_sum = 0
        for num in sub_nums:
            sub_sum += num

        if sub_sum < min_sum:
            min_sum = sub_sum

        if sub_sum > max_sum:
            max_sum = sub_sum
    gap = max_sum - min_sum
    print(f"#{test_case} {gap}")
