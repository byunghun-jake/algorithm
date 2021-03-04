# 1. 길이가 10(0~9)인 카운팅 리스트를 만든다.
# 2. 카드 목록을 순환하며, 카운팅 리스트에 갯수를 담는다.
# 3. 카운팅 리스트를 순환하며, 가장 값이 클 때를 찾는다.
# 4. 카운팅 리스트를 역순환하며, 가장 큰 값과 같을 때 그 인덱스를 반환한다.

import sys

sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    card_count = int(input())
    card_list = input()
    card_count_list = [0] * 10
    result = 0

    for i in range(card_count):
        index = int(card_list[i])
        card_count_list[index] += 1

    max_count = 0
    for idx in range(len(card_count_list)):
        count = card_count_list[idx]
        if max_count < count:
            max_count = count

    for idx in range(len(card_count_list) - 1, -1, -1):
        count = card_count_list[idx]
        if max_count == count:
            result = idx
            break

    print(f"#{test_case} {result} {max_count}")
