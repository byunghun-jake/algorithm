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

    # 1. 가장 적은 횟수로 만들 수 있는 가장 큰 수
    # 같은 값과 교환된 값을 서로 비교해 자리를 바꿔주는 조건?
    # 같은 값과 교환된 값의 위치를 리스트에 담아두자
    i = 0
    count = 0
    b_num = 0
    index_list = []
    while count < change_count and i < N:
        b_index = i
        for j in range(i+1, N):
            if num_list[j] >= num_list[b_index]:
                b_index = j

        # 교환하는 최대값이 변했는지 확인
        if num_list[b_index] != b_num:
            # 변했다면, 지금까지 index_list에 있는 값들을 비교, 정렬
            sub_length = len(index_list)
            if sub_length > 1:
                # 내림차순 선택 정렬
                for sub_i in range(sub_length-1):
                    sub_max_index = sub_i
                    for sub_j in range(sub_i+1, sub_length):
                        if num_list[sub_j] > num_list[sub_max_index]:
                            sub_max_index = sub_j
                    num_list[sub_i], num_list[sub_max_index] = num_list[sub_max_index], num_list[sub_i]
            # 인덱스 리스트 초기화
            index_list = []
            b_num = num_list[b_index]

        # 교환 진행
        if i != b_index:
            num_list[i], num_list[b_index] = num_list[b_index], num_list[i]
            index_list.append(b_index)      # 교체된 인덱스의 값을 담는다
            count += 1                      # 교체 카운트를 1 증가시킨다

        i += 1                              # 다음 인덱스로 넘어간다

    # 정렬 종료 후
    # 1. 교환 횟수가 남아있는 경우
    remain_count = change_count - count
    is_duplicated_num = False
    counting_list = [0]*10
    for num in num_list:
        counting_list[num] += 1
        if counting_list[num] > 1:
            is_duplicated_num = True
            break
    # 1-1. 교환 횟수가 짝수라면, 추가 정렬 필요 없음
    # 1-2. 교환 횟수가 홀수라면, 변화 값이 최소가 되도록 추가 교환
    if remain_count % 2 and not is_duplicated_num:
        # 1-2-1. 동일한 값이 2개 이상이라면, 추가 정렬 필요 없음
        # 1-2-2. 동일한 값이 없다면, 마지막 두 값을 교환
        num_list[N-2], num_list[N-1] = num_list[N-1], num_list[N-2]

    # 정렬이 종료된 후 index_list를 확인한다.
    if len(index_list) > 1:
        # 오름차순 선택 정렬 (index_list가 뒤집어져 있어서)
        for i in range(len(index_list) - 1):
            idx = index_list[i]
            min_idx = idx
            for j in range(i + 1, len(index_list)):
                n_idx = index_list[j]
                a = num_list[n_idx]
                b = num_list[min_idx]
                if a < b:
                    min_idx = n_idx
            num_list[idx], num_list[min_idx] = num_list[min_idx], num_list[idx]

    # 정렬한 수열을 숫자로 변환합니다.
    result = 0
    for i in range(N):
        result += num_list[i] * (10 ** (N - i - 1))

    print(f"#{C} {result}")



