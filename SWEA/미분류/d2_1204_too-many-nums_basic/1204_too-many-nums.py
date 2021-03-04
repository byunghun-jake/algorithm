# 1. 0점 이상 100점 이하이므로 101개의 요소를 갖는 카운팅 리스트를 만든다.
# 2. 스코어 리스트를 순환하며, 카운팅 리스트 값을 증가시킨다.
# 3. 카운팅 리스트를 순환하며, 카운팅 최대 값을 찾는다.
# 4. 카운팅 리스트를 역순환하며, 카운팅 최대 값에 해당하는 인덱스 값을 찾으면, 반복문을 탈출하고 반환한다.

import sys

sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    test_num = int(input())
    score_list = list(map(int, input().split()))
    counting_list = [0] * 101
    max_count_num = 0
    max_count = 0

    for score in score_list:
        counting_list[score] += 1

    for count in counting_list:
        if count > max_count:
            max_count = count

    for idx in range(len(counting_list) - 1, -1, -1):
        if counting_list[idx] == max_count:
            max_count_num = idx
            break

    print(f"#{test_num} {max_count_num}")
