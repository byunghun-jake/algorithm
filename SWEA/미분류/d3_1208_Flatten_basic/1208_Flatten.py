# 1. 한번 쭉 순환하면서 최소높이와 최대 높이를 찾아보자
# 2. 덤프 횟수 만큼 순환하자
# 2-1. 최소 높이와 일치하는 높이를 찾아 1을 추가한다.
# 2-2. 최대 높이와 일치하는 높이를 찾아 1을 빼준다.
# 2-3. 최소 높이와 최대 높이를 다시 찾아보자 (1번)
# 3. 최소 높이와 최대 높이의 차를 반환하자.

import sys

sys.stdin = open("./input.txt")


def get_min_max(h_list):
    min_h = 100
    max_h = 1
    for height in h_list:
        if height < min_h:
            min_h = height
        elif height > max_h:
            max_h = height
    return min_h, max_h


for test_case in range(1, 11):
    dump_count = int(input())
    height_list = list(map(int, input().split()))

    min_height, max_height = get_min_max(height_list[:])

    for i in range(dump_count):
        for idx in range(len(height_list)):
            if height_list[idx] == min_height:
                height_list[idx] += 1
                break
        for idx in range(len(height_list)):
            if height_list[idx] == max_height:
                height_list[idx] -= 1
                break

        min_height, max_height = get_min_max(height_list[:])

    result = max_height - min_height
    print(f"#{test_case} {result}")
