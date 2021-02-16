# 역순으로 정렬하면 되지 않을까?
# 선택정렬을 뒤집어서 활용해보자

import sys

sys.stdin = open("input.txt")

T = int(input())
for C in range(1, T + 1):
    # NUM: 정렬할 숫자
    # change_count: 정렬 가능 횟수
    NUM, change_count = map(int, input().split())

    # 숫자 NUM을 배열로 변환한다.
    num_as_str = str(NUM)
    N = len(num_as_str)
    num_list = [int(num_as_str[i]) for i in range(N)]
    # print(num_list)

    # 정렬 가능 횟수만큼 선택정렬을 수행합니다.
    # TC 2번을 보고, 선택정렬로만 수행하면 제대로 문제를 풀 수 없음을 알 수 있었다.
    # 값을 교환하지 않았을 때, 교환 카운트가 되면 안된다.
    change_count = change_count if len(num_as_str) > change_count else N
    count = 0
    i = 0
    while count != change_count and i < N:
        max_index = i
        for j in range(i+1, N):
            if num_list[j] >= num_list[max_index]:       # 이 조건에 등호를 추가해주어야 한다
                max_index = j
        if i != max_index:
            num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
            count += 1
        i += 1

    # 정렬한 수열을 숫자로 변환합니다.
    result = 0
    for i in range(N):
        result += num_list[i] * (10**(N-i-1))

    print(f"#{C} {result}")






